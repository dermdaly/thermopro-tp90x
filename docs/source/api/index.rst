API Reference
=============

Core library for BLE communication with TP902 thermometer.

Overview
--------

TP902 provides a lightweight Python library for communicating with ThermoPro TP902 wireless thermometer over BLE.
The library includes:

* **Main Protocol Class** - :class:`~tp902.TP902` for device communication
* **Transport Layer** - Abstract :class:`~tp902.TP902Transport` base class for BLE implementations
* **Data Classes** - Structured results (Temperature, AlarmConfig, FirmwareVersion, etc.)
* **Packet Helpers** - Utilities for temperature encoding, packet building, and checksum verification
* **Constants** - BLE UUIDs, command codes, and value constants

Quick Reference
---------------

Main Classes
^^^^^^^^^^^^

.. autosummary::
   :nosignatures:

   tp902.TP902
   tp902.TP902Transport

Data Classes
^^^^^^^^^^^^

.. autosummary::
   :nosignatures:

   tp902.Temperature
   tp902.TemperatureBroadcast
   tp902.TemperatureActual
   tp902.AlarmConfig
   tp902.FirmwareVersion
   tp902.DeviceStatus
   tp902.AuthResponse

Packet Helpers
^^^^^^^^^^^^^^

.. autosummary::
   :nosignatures:

   tp902.build_packet
   tp902.verify_checksum
   tp902.decode_temp_bcd
   tp902.encode_temp_bcd

Detailed Documentation
----------------------

.. toctree::
   :maxdepth: 2

   tp902
   data_classes
   helpers
   transport
