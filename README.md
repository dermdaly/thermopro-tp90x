# ThermoPro TP902

BLE parser for ThermoPro TP902 wireless thermometer.

**Protocol sources:** Device behavior (Observed) and APK decompilation (Implementation).

## Documentation

- **[Protocol Specification](PROTOCOL.md)** - Detailed BLE protocol notes and frame formats
- **[Register Reference](REGISTERS.md)** - Complete register specifications and data structures
- **[API Documentation](docs/)** - Sphinx documentation with API reference and examples

## Quick Start

Installation:

```bash
pip install thermopro-tp902
```

Basic usage with bleak:

```python
from bleak import BleakClient
from tp902 import TP902, TP902Transport

class MyTransport(TP902Transport):
    def __init__(self, client):
        self.client = client

    async def send(self, data):
        await self.client.write_gatt_char(TP902.WRITE_UUID, data)

    async def receive(self, timeout_ms):
        # Implement timeout handling for your platform
        pass

# Usage
async with BleakClient(address) as client:
    transport = MyTransport(client)
    tp = TP902(transport)
    await tp.authenticate()
    status = await tp.get_status()
    print(status)
```

## Examples

See [examples](examples/) directory for working examples with bleak and other platforms.
