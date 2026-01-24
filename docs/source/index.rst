ThermoPro TP902 Documentation
=============================

BLE parser for ThermoPro TP902 wireless thermometer.

**Protocol sources:** Device behavior (Observed) and APK decompilation (Implementation).

Quick Start
-----------

Installation:

.. code-block:: bash

   pip install thermopro-tp902

Basic usage with bleak:

.. code-block:: python

   from bleak import BleakClient
   from tp902 import TP902, TP902Transport

   class MyTransport(TP902Transport):
       def __init__(self, client):
           self.client = client
       async def send(self, data):
           await self.client.write_gatt_char(TP902.WRITE_UUID, data)
       async def recv(self):
           return await self.client.start_notify(TP902.NOTIFY_UUID, lambda _, data: data)

Documentation
-------------

.. toctree::
   :maxdepth: 2
   :caption: Documentation:

   protocol
   registers
   api/index
   examples

Quick Links
-----------

* `Protocol Specification <protocol.html>`_ - Detailed BLE protocol notes
* `Register Reference <registers.html>`_ - Frame formats and register details
* `API Reference <api/index.html>`_ - Library API documentation
* `Examples <examples.html>`_ - Usage examples and code snippets

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
