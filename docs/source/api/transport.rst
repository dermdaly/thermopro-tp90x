Transport Layer
===============

Advanced extension points for custom BLE integration.

TP90xTransport
--------------

.. autoclass:: tp90x.tp90xbase.TP90xTransport
   :members:
   :undoc-members:
   :show-inheritance:

Implementation
~~~~~~~~~~~~~~

Subclass and implement :meth:`~tp90x.tp90xbase.TP90xTransport.send` and
:meth:`~tp90x.tp90xbase.TP90xTransport.receive` for your platform.

Most users should prefer :meth:`tp90x.tp90xbase.TP90xBase.connect` and avoid
custom transport plumbing.

Example skeleton:

.. code-block:: python

   from tp90x.tp90xbase import TP90xTransport

   class MyTransport(TP90xTransport):
       def send(self, data):
           ...

       def receive(self, timeout_ms):
           ...
