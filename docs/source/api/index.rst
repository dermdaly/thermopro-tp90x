API Reference
=============

Core library for BLE communication with TP90x thermometers.

Overview
--------

This section is generated from module/class docstrings using Sphinx autodoc.
The primary public API includes:

* **Model classes** - :class:`~tp90x.TP902` and :class:`~tp90x.TP904`
* **Enums** - :class:`~tp90x.AlarmMode` and :class:`~tp90x.SearchMode`
* **Data classes** - structured response objects
* **Advanced internals** - :class:`~tp90x.tp90xbase.TP90xBase` and :class:`~tp90x.tp90xbase.TP90xTransport`

Quick Reference
---------------

Main Classes
^^^^^^^^^^^^

.. autosummary::
   :nosignatures:

   tp90x.TP902
   tp90x.TP904
   tp90x.SearchMode
   tp90x.AlarmMode

Data Classes
^^^^^^^^^^^^

.. autosummary::
   :nosignatures:

   tp90x.Temperature
   tp90x.TemperatureBroadcast
   tp90x.TemperatureActual
   tp90x.AlarmConfig
   tp90x.FirmwareVersion
   tp90x.DeviceStatus
   tp90x.AuthResponse

Detailed Documentation
----------------------

.. toctree::
   :maxdepth: 2

   tp902
   data_classes
   helpers
   transport
