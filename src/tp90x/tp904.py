"""TP904 concrete model implementation."""

from .tp90xbase import TP90xBase


class TP904(TP90xBase):
    """ThermoPro TP904 protocol model."""

    NUM_PROBES = 2

    @classmethod
    def model_name(cls):
        """Return stable model identifier."""
        return "TP904"
