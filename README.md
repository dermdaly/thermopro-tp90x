# ThermoPro TP902

Parser and test data for TP902 thermometer

**Protocol sources:** Device behavior (Observed) and APK decompilation (Implementation).

## Protocol notes

TX (write to `1086fff1`):
- `0x01` auth handshake (randomized payload)
- `0x20` set units (payload `0x0c`=C, `0x0f`=F)
- `0x21` sound alarm enable (payload `0x0c`=ON, `0x0f`=OFF)
- `0x23` set alarm (ch, mode, BCD temps)
- `0x24` read alarm for channel (payload: channel 1-6)
- `0x26` get status (no data; response: units, beeper, battery)
- `0x27` request (no data; effect unclear, not used in APK)
- `0x28` time sync (epoch seconds since 2020-01-01)
- `0x41` read fw version

RX (notify on `1086fff2`):
- `0x30` temp broadcast: byte2=battery, byte3=units (`0x0c`=C, `0x0f`=F),
  byte4=deviceAlarms, bytes5.. temps (BCD, sign in bit7), `ffff`=no probe.
- `0x25` temp snapshot (on-demand): byte2=probe count, byte3=deviceAlarms,
  bytes4.. temps (same BCD as 0x30).
- `0x26` status/config: byte2=units (`0x0c`=C, `0x0f`=F), byte3=beeper
  (`0x0c`=ON, `0x0f`=OFF), byte4=battery.
- `0x24` alarm read: byte2=channel (1-based), byte3=mode/index,
  bytes4.. temps (target/range).
- `0x41` fw version: byte2 BCD `X.Y`.
- `0x01` auth response: bytes map device type/probe count (unknown mapping).
- `0xe0` ack/trigger (no parsing in app).

Not seen in app code: `0x02`, `0x03`, `0x29`, `0x42`.

Observed behavior: see `PROTOCOL.md`.
