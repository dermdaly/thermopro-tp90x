TP902 BLE protocol notes
=========================

**Note:** Protocol details from device behavior (Observed) and APK decompilation (Implementation).

Packet format
-------------

Frame: `CMD LEN DATA[LEN] CHECKSUM`.
- `CMD`: 1 byte.
- `LEN`: 1 byte length of DATA.
- `DATA`: payload.
- `CHECKSUM`: `sum(frame[0:2+LEN]) & 0xFF`.

Notifications are typically 20 bytes long; bytes past `2+LEN+1` are padding.

Services/characteristics
------------------------

- Service: `1086fff0-3343-4817-8bb2-b32206336ce8`
- Write:   `1086fff1-3343-4817-8bb2-b32206336ce8`
- Notify:  `1086fff2-3343-4817-8bb2-b32206336ce8`

Temperature encoding
--------------------

2-byte BCD, tenths of °C.
`FFFF` means probe not present.

Known commands
--------------

Write (TX)
~~~~~~~~~~

- `0x01` auth handshake (randomized payload).
- `0x20` set units (`0x0c`=C, `0x0f`=F).
- `0x21` sound alarm enable (`0x0c`=ON, `0x0f`=OFF).
- `0x23` set alarm (ch, mode, BCD temps).
- `0x24` read alarm for channel (`ch+1`).
- `0x26` get status (no data).
- `0x27` request (no data; effect unclear, not used in APK).
- `0x28` time sync (epoch seconds since 2020-01-01).
- `0x41` read fw version.

Notify (RX)
~~~~~~~~~~~

- `0x30` temp broadcast: `data[0]` battery, `data[1]` units (`0x0c`=C,
  `0x0f`=F), `data[2]` deviceAlarms, `data[3..]` temps.
- `0x25` temp snapshot: `data[0]` probe count, `data[1]` deviceAlarms,
  `data[2..]` temps.
- `0x26` status/config: `data[0]` units (`0x0c`=C, `0x0f`=F), `data[1]` beeper
  (`0x0c`=ON, `0x0f`=OFF), `data[2]` battery (0-100%).
- `0x24` alarm read: `data[0]` channel (1-based), `data[1]` mode/index,
  `data[2..]` temps (target/range).
- `0x41` fw version: `data[0]` BCD `X.Y`.
- `0x01` auth response: maps device type/probe count (mapping unknown).
- `0xe0` ack/trigger (no parsing in app).

Unknown commands (respond with data)
------------------------------------

These return data but are not parsed in app code.

- `0x02` `len=0` (ack/keepalive).
- `0x03` `len=1` `data=00` (status/flags).
- `0x27` `len=0` (ack).
- `0x29` `len=9` (all zeros observed).
- `0x42` `len=1` (value `0x02` observed).
- `0x26` `len=5` data present (parsed only as units/flags/battery above).
- `0x25` `len=14` data present (parsed as temps snapshot above).

Observed behavior
-----------------

- Setting a target equal to the current alarm threshold triggers an alarm
  only if the target value changed (from a different value). If the target
  stays the same, no new alarm is raised. Unsure if re-arming needs HW button.
- While `deviceAlarms` is non-zero, toggling `0x21`:
  - ON: starts beeping (flag stays set).
  - OFF: stops beeping and clears `deviceAlarms`.
- With beep OFF, the device still flashes the display. Pressing the hardware
  button clears the alarm and resets `deviceAlarms` to 0.
- Alarm re-triggers after returning to the safe zone and crossing the
  threshold again (no retrigger while staying beyond the limit).
