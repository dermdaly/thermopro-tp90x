from enum import Enum


class AlarmMode(Enum):
    Off = 0
    Target = 1
    Range = 2


class SearchMode(Enum):
    ADDRESS = "address"
    NAME = "name"
