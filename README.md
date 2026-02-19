# ThermoPro TP90x

BLE parser for ThermoPro TP90x wireless thermometers.

**Protocol sources:** Device behavior (Observed) and APK decompilation (Implementation).

## Attribution

This project is derived from the original ThermoPro TP902 work by Petr Kracik:
- https://github.com/petrkracik/thermopro-tp902

The current codebase has been refactored for TP90x multi-model support.

## Documentation

- **[Protocol Specification](PROTOCOL.md)** - Detailed BLE protocol notes and frame formats
- **[Register Reference](REGISTERS.md)** - Complete register specifications and data structures
- **[API Documentation](docs/)** - Sphinx documentation with API reference and examples

## Quick Start

Installation:

```bash
pip install thermopro-tp90x
```

Basic usage with built-in connect:

```python
from tp90x import SearchMode, TP902

with TP902.connect("AA:BB:CC:DD:EE:FF", by=SearchMode.ADDRESS) as tp:
    auth = tp.authenticate()
    status = tp.get_status()
    print(auth, status)
```

## Examples

See [examples](examples/) directory for working examples with bleak and other platforms.
