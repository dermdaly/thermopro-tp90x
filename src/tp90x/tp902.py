from .tp90xbase import TP90xBase


class TP902(TP90xBase):
    NUM_PROBES = 6

    @classmethod
    def model_name(cls):
        return "TP902"
