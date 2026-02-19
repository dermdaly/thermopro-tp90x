"""Public API for the tp90x package."""

from .enums import AlarmMode
from .tp902 import TP902
from .tp904 import TP904
from .tp90xbase import (
    TP90xBase,
    TP90xTransport,
    AlarmConfig,
    AuthResponse,
    DeviceStatus,
    FirmwareVersion,
    Temperature,
    TemperatureActual,
    TemperatureBroadcast,
    build_packet,
    decode_temp_bcd,
    encode_temp_bcd,
    verify_checksum,
)

__all__ = [
    "TP90xBase",
    "TP90xTransport",
    "TP902",
    "TP904",
    "AlarmMode",
    "Temperature",
    "TemperatureBroadcast",
    "TemperatureActual",
    "AlarmConfig",
    "FirmwareVersion",
    "DeviceStatus",
    "AuthResponse",
    "build_packet",
    "verify_checksum",
    "decode_temp_bcd",
    "encode_temp_bcd",
]
