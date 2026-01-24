# TP902 Usage Examples

This directory contains example scripts demonstrating how to use the ThermoPro TP902 library.

## Bleak Example (Linux/macOS/Windows)

The `bleak_example.py` script shows how to communicate with a TP902 device using the [bleak](https://bleak.readthedocs.io/) BLE library, which works across multiple platforms.

### Installation

```bash
pip install bleak thermopro-tp902
```

### Running the Example

First, find your TP902 device's BLE address using your OS tools:

**Linux (bluetoothctl):**
```bash
bluetoothctl
> scan on
# Look for your TP902 device (e.g., "TP902-XXXX")
> scan off
```

**macOS (system-profiler):**
```bash
system_profiler SPBluetoothDataType
```

**Windows (Settings):**
Open Settings → Devices → Bluetooth & devices → to see paired devices.

Then run the example:

```bash
python bleak_example.py <BLE_ADDRESS>
```

Example:
```bash
python bleak_example.py AA:BB:CC:DD:EE:FF
```

### What the Example Does

The example performs the following steps:

1. **Scans** for the device by BLE address
2. **Connects** to the device (up to 20 seconds)
3. **Authenticates** with the device
4. **Reads firmware version** from device
5. **Reads alarm configuration** for channel 1
6. **Reads device status** (battery, channels, etc.)
7. **Listens** for temperature broadcasts continuously

Temperature updates are printed as they arrive. Press `Ctrl+C` to stop.

## Transport Implementation

The example includes a `BleakTransport` class that bridges between bleak's async API and the synchronous TP902 API.

### Design Details

- **`send(data: bytes)`** - Sends data to the device via a GATT write characteristic. Runs in the asyncio event loop via `run_coroutine_threadsafe()`.
- **`receive(timeout_ms: int)`** - Receives data from a queue populated by BLE notifications. Blocks until data arrives or timeout.
- **`on_notify(handle, data)`** - Called by bleak when notifications arrive. Queues the data for `receive()`.
- **Threading model** - The TP902 session runs in a daemon thread while the asyncio event loop runs in the main thread. This allows the synchronous TP902 API to work alongside bleak's async API.

### Using BleakTransport in Your Code

```python
from bleak import BleakClient
from tp902 import TP902, SERVICE_UUID, WRITE_UUID, NOTIFY_UUID
from examples.bleak_example import BleakTransport

async with BleakClient(device) as client:
    transport = BleakTransport(client, asyncio.get_running_loop())
    await client.start_notify(NOTIFY_UUID, transport.on_notify)

    # Run TP902 in a thread
    tp = TP902(transport)
    auth = tp.authenticate()
    # ... use tp902 API
```
