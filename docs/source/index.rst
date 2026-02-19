ThermoPro TP90x Documentation
=============================

BLE parser for ThermoPro TP90x wireless thermometers.

**Protocol sources:** Device behavior (Observed) and APK decompilation (Implementation).

Quick Start
-----------

Installation:

.. code-block:: bash

   pip install thermopro-tp90x[bleak]

Basic usage with bleak:

.. code-block:: python

   from tp90x import TP902, SearchMode

   with TP902.connect("AA:BB:CC:DD:EE:FF", by=SearchMode.ADDRESS) as tp:
       auth = tp.authenticate()
       status = tp.get_status()
       print(auth, status)

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
