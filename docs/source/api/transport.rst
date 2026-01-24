Transport Layer
===============

Abstract base class for BLE transport implementations.

TP902Transport
--------------

.. autoclass:: tp902.TP902Transport
   :members:
   :undoc-members:
   :show-inheritance:

Implementation
~~~~~~~~~~~~~~

Subclass and implement :meth:`~tp902.TP902Transport.send` and :meth:`~tp902.TP902Transport.receive` for your platform.

Example with bleak:

.. code-block:: python

   from bleak import BleakClient
   from tp902 import TP902, TP902Transport

   class BleakTransport(TP902Transport):
       def __init__(self, client):
           self.client = client
           self._notification = None

       async def send(self, data):
           await self.client.write_gatt_char(TP902.WRITE_UUID, data)

       async def receive(self, timeout_ms):
           # Implement timeout handling for your platform
           # Return bytes from notification or None on timeout
           pass
