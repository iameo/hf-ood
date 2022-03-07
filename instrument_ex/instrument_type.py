from enum import Enum

class InstrumentType(Enum):
    GUITAR = "Guitar"
    BANJO = "Banjo"
    MANDOLIN = "Mandolin"
    BASS = "Bass"

    def __str__(self):
        return str(self.value)