TP902 registry/frames
=====================

**Note:** Frame specifications from device behavior (Observed) and APK decompilation (Implementation).

Packet format
-------------

`CMD LEN DATA[LEN] CHECKSUM`

DATA offsets are relative to `DATA[0]` (i.e. after `CMD` and `LEN`).

Summary table
-------------

| CMD | Dir | LEN | Meaning | Source |
| --- | --- | --- | ------- | ------ |
| 0x01 | TX/RX | 0x0b/0x02 | auth | Implementation |
| 0x02 | RX | 0x00 | unknown | Observed |
| 0x03 | RX | 0x01 | unknown | Observed |
| 0x20 | TX | 0x01 | set units | Implementation |
| 0x21 | TX | 0x01 | sound alarm | Implementation |
| 0x23 | TX | 0x06 | alarm set | Implementation |
| 0x24 | TX/RX | 0x01/0x06 | alarm read/response | Implementation |
| 0x25 | RX | 0x0e | temp snapshot | Implementation |
| 0x26 | TX/RX | 0x00/0x05 | get status | Implementation |
| 0x27 | TX | 0x00 | request (trigger) | Observed |
| 0x28 | TX | 0x04 | time sync | Implementation |
| 0x29 | RX | 0x09 | unknown | Observed |
| 0x30 | RX | 0x0f | temp broadcast | Implementation |
| 0x41 | TX/RX | 0x00/0x03 | fw version | Implementation |
| 0x42 | RX | 0x01 | unknown | Observed |
| 0xe0 | RX | 0x02 | Error | Observed |

0x01 (auth)
-----------

**TX:** `LEN=0x09` (randomized payload with lookup tables).

**RX:** `LEN=0x02`
- `DATA[0..1]` auth response (maps device type/probe count; mapping unknown).
Source: Implementation.

0x20 (set units)
----------------

**TX:** `LEN=0x01`
- `DATA[0]` `0x0c`=C, `0x0f`=F.
Source: Implementation.

0x21 (sound alarm)
------------------

**TX:** `LEN=0x01`
- `DATA[0]` `0x0c`=ON, `0x0f`=OFF.
Source: Implementation.

0x23 (alarm set)
----------------

**TX:** `LEN=0x06`
- `DATA[0]` channel (1-6).
- `DATA[1]` mode (`0x00`=OFF, `0x0a`=TARGET, `0x82`=RANGE).
- `DATA[2..5]` temps (2 * 2B BCD: value1 / value2).
Source: Implementation.

0x24 (alarm read)
-----------------

**Request:** `LEN=0x01`
- `DATA[0]` channel (1-6).

**Response:** `LEN=0x06`
- `DATA[0]` channel (1-6).
- `DATA[1]` mode (`0x00`=OFF, `0x0a`=TARGET, `0x82`=RANGE).
- `DATA[2..5]` temps (2 * 2B BCD: value1 / value2).
Source: Implementation.

0x25 (temp snapshot)
--------------------

**RX:** `LEN=0x0e`
- `DATA[0]` probe count (typically `0x06`).
- `DATA[1]` deviceAlarms (alarm state, not confirmed).
- `DATA[2..13]` T1..T6 (6 * 2B BCD, `FFFF` = empty).
Source: Implementation.

0x26 (get status)
-----------------

**Request:** `LEN=0x00` (no data).

**Response:** `LEN=0x05`
- `DATA[0]` units (`0x0c`=C, `0x0f`=F).
- `DATA[1]` beeper (`0x0c`=ON, `0x0f`=OFF).
- `DATA[2]` battery (0-100%).
- `DATA[3..4]` padding.
Source: Implementation.

0x27 (request/trigger)
----------------------

**TX:** `LEN=0x00` (no data). Effect unclear; device returns empty response. Not used in APK.
Source: Observed.

0x28 (time sync)
----------------

**TX:** `LEN=0x04`
- `DATA[0..3]` seconds since 2020-01-01 (little-endian).
Source: Implementation.

0x30 (temp broadcast)
----------------------

**RX:** `LEN=0x0f`
- `DATA[0]` battery (0-100).
- `DATA[1]` units (`0x0c`=C, `0x0f`=F).
- `DATA[2]` deviceAlarms (alarm state, not confirmed).
- `DATA[3..14]` T1..T6 (6 * 2B BCD, `FFFF` = empty).
Source: Implementation.

0x41 (fw version)
-----------------

**TX:** `LEN=0x00` (no data).

**RX:** `LEN=0x03`
- `DATA[0]` BCD `X.Y`.
- `DATA[1..2]` minor/build (format unknown).
Source: Implementation.

Unknown (responds with data)
----------------------------

- `0x02` `LEN=0` (ack/keepalive?), source: Observed.
- `0x03` `LEN=1` `DATA[0]=0x00`, source: Observed.
- `0x29` `LEN=9` (all zeros observed), source: Observed.
- `0x42` `LEN=1` (value `0x02` observed), source: Observed.
