"""TP902 concrete model implementation."""

from .tp90xbase import TP90xBase


class TP902(TP90xBase):
    """ThermoPro TP902 protocol model."""

    NUM_PROBES = 6

    @classmethod
    def model_name(cls):
        """Return stable model identifier."""
        return "TP902"
