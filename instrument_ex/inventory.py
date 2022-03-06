from instrument import Instrument
from instrument_spec import InstrumentSpec


class Inventory:
    def __init__(self):
        self._instruments = list()
        
    def add_instrument(self, serialNum, price, instrument_spec: InstrumentSpec):
        instrument = Instrument(serialNum, price, instrument_spec)
        self._instruments.append(instrument)
        return
    
    def get_instrument_by_serial_num(self, serialNum):
        for instrument in self._instruments:
            if instrument.serialNum.lower() == serialNum.lower():
                return instrument
        return False
     
    def search(self, other_spec: InstrumentSpec) -> list:
        similar_instruments = list()
        
        for instrument in self._instruments:
            if instrument.get_spec().matches(other_spec):
                similar_instruments.append(instrument)
            else:
                continue
        return similar_instruments
    
    def instruments(self):
        return self._instruments
    
    def __repr__(self):
        return f'{self._instruments}'
            
        