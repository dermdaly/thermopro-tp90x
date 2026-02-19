# TP90x Usage Examples

This directory contains runnable examples for the ThermoPro TP90x package.

## Install

```bash
pip install "thermopro-tp90x[bleak]"
```

## Example Scripts

- `bleak_example.py`: TP902 example (search/connect by BLE address)
- `tp904_example.py`: TP904 example (search/connect by advertised name)
- `interactive_example.py`: interactive menu for TP902/TP904 with command actions

## Running

TP902 by address:

```bash
python examples/bleak_example.py AA:BB:CC:DD:EE:FF
```

TP904 by name:

```bash
python examples/tp904_example.py TP904-XXXX
```

Interactive menu:

```bash
python examples/interactive_example.py
```

## Notes

- The examples use the high-level `connect()` API; users do not need to manage BLE UUIDs or transport internals.
- Model-specific behavior differences should be documented in `PROTOCOL.md` and `REGISTERS.md` as they are confirmed.
