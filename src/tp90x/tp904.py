from .tp90xbase import TP90xBase


class TP904(TP90xBase):
    NUM_PROBES = 2

    @classmethod
    def model_name(cls):
        return "TP904"

    