#!/usr/bin/env python3
"""TP902 high-level example using built-in connect()."""

from __future__ import annotations

import argparse

from tp90x import SearchMode, TP902, TemperatureBroadcast


def on_temperature(broadcast: TemperatureBroadcast) -> None:
    print(broadcast)


def main() -> int:
    parser = argparse.ArgumentParser(description="TP902 high-level example")
    parser.add_argument("address", help="BLE address of TP902 device")
    parser.add_argument("--scan-timeout", type=float, default=10.0)
    args = parser.parse_args()

    with TP902.connect(
        args.address,
        by=SearchMode.ADDRESS,
        scan_timeout=args.scan_timeout,
        on_temperature=on_temperature,
    ) as tp:
        auth = tp.authenticate()
        if auth is None:
            print("Auth timeout!")
            return 1
        print("Authenticated:", auth)

        fw = tp.get_firmware_version()
        if fw:
            print("Firmware:", fw)

        status = tp.get_status()
        if status:
            print("Status:", status)

        print("Listening for broadcasts (Ctrl+C to stop)...")
        while True:
            tp.process(timeout_ms=1000)


if __name__ == "__main__":
    raise SystemExit(main())
