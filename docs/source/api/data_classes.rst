Data Classes
=============

Structured results returned by TP90x methods.

Temperature
-----------

.. autoclass:: tp90x.Temperature
   :members:
   :undoc-members:
   :show-inheritance:

TemperatureBroadcast
--------------------

Periodic temperature broadcast (command 0x30).

.. autoclass:: tp90x.TemperatureBroadcast
   :members:
   :undoc-members:
   :show-inheritance:

TemperatureActual
-----------------

On-demand temperature reading (command 0x25).

.. autoclass:: tp90x.TemperatureActual
   :members:
   :undoc-members:
   :show-inheritance:

AlarmConfig
-----------

Alarm configuration for a channel.

.. autoclass:: tp90x.AlarmConfig
   :members:
   :undoc-members:
   :show-inheritance:

FirmwareVersion
---------------

Device firmware version information.

.. autoclass:: tp90x.FirmwareVersion
   :members:
   :undoc-members:
   :show-inheritance:

DeviceStatus
------------

Device status and configuration.

.. autoclass:: tp90x.DeviceStatus
   :members:
   :undoc-members:
   :show-inheritance:

AuthResponse
------------

Authentication handshake response.

.. autoclass:: tp90x.AuthResponse
   :members:
   :undoc-members:
   :show-inheritance:
