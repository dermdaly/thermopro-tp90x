#!/usr/bin/env python3
"""TP902 example using bleak BLE library (Linux/macOS/Windows).

Usage:
    python bleak_example.py <BLE_ADDRESS>
"""
from __future__ import annotations

import argparse
import asyncio
import queue
import sys
import os
import threading
from tp90x import TP902, TP90xTransport, TemperatureBroadcast
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bleak import BleakClient, BleakScanner


class BleakTransport(TP90xTransport):
    """TP902 transport over bleak BLE client.

    Designed to be used from a thread (via run_in_executor) while
    the asyncio event loop runs in the main thread.
    """

    def __init__(self, client: BleakClient, loop: asyncio.AbstractEventLoop):
        self._client = client
        self._loop = loop
        self._queue: queue.Queue = queue.Queue()
        self._stop_event = threading.Event()

    def send(self, data: bytes) -> None:
        fut = asyncio.run_coroutine_threadsafe(
            self._client.write_gatt_char(TP902.WRITE_UUID, data, response=True),
            self._loop,
        )
        fut.result(timeout=10.0)

    def receive(self, timeout_ms: int) -> bytes | None:
        try:
            return self._queue.get(timeout=timeout_ms / 1000.0)
        except queue.Empty:
            return None

    def on_notify(self, _handle: int, data: bytearray) -> None:
        """BLE notification callback. Call from bleak's start_notify."""
        self._queue.put(bytes(data))

    def should_stop(self) -> bool:
        """Check if stop event was signaled."""
        return self._stop_event.is_set()

    def stop(self) -> None:
        """Signal stop event from async context."""
        self._stop_event.set()


def on_temperature(broadcast: TemperatureBroadcast) -> None:
    """Called on every 0x30 temperature broadcast."""
    print(broadcast)


def run_tp902(transport: BleakTransport) -> None:
    """Blocking TP902 session. Runs in a thread."""
    tp = TP902(transport, on_temperature=on_temperature)

    # Authenticate
    auth = tp.authenticate()
    if auth is None:
        print("Auth timeout!")
        return
    print("Authenticated:", auth)

    # Get firmware version
    fw = tp.get_firmware_version()
    if fw:
        print("Firmware:", fw)

    # Read alarm config for channel 1
    alarm = tp.get_alarm(1)
    if alarm:
        print("Alarm ch1:", alarm)

    # Get device status
    status = tp.get_status()
    if status:
        print("Status:", status)

    # Continuous processing - listen for broadcasts
    print("Listening for temperature broadcasts (Ctrl+C to stop)...",
          file=sys.stderr)
    while not transport.should_stop():
        tp.process(timeout_ms=1000)


async def main() -> int:
    parser = argparse.ArgumentParser(description="TP902 bleak example")
    parser.add_argument("address", help="BLE address of TP902 device")
    parser.add_argument("--timeout", type=float, default=10.0,
                        help="Scan timeout (seconds)")
    args = parser.parse_args()

    print("Scanning for %s..." % args.address)
    device = await BleakScanner.find_device_by_address(
        args.address, timeout=args.timeout
    )
    if not device:
        print("Device not found.")
        return 2

    loop = asyncio.get_running_loop()

    async with BleakClient(device, timeout=20.0, services=[TP902.SERVICE_UUID]) as client:
        print("Connected: %s (%s)" % (device.address, device.name))

        transport = BleakTransport(client, loop)
        await client.start_notify(TP902.NOTIFY_UUID, transport.on_notify)

        # Run TP902 in daemon thread
        def run_thread():
            run_tp902(transport)

        thread = threading.Thread(target=run_thread, daemon=True)
        thread.start()

        try:
            # Just wait for thread to finish or interrupt
            while thread.is_alive():
                await asyncio.sleep(0.1)
        except KeyboardInterrupt:
            print("\nInterrupted.")
            transport.stop()
            # Give thread a moment to exit gracefully
            thread.join(timeout=1.0)
        finally:
            try:
                await client.stop_notify(TP902.NOTIFY_UUID)
            except Exception:
                pass

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(asyncio.run(main()))
    except KeyboardInterrupt:
        pass
