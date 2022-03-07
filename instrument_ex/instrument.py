from instrument_spec import InstrumentSpec

class Instrument:
    def __init__(self, serialNum: str, price: float, spec: InstrumentSpec):
        self.serialNum = serialNum
        self.price = price
        self.spec = spec
    
    def get_serial_num(self):
        return self.serialNum
    
    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price
    
    def get_spec(self) -> InstrumentSpec:
        return self.spec

    def __repr__(self):
        return f'{self.__class__.__name__}({self.serialNum}, {self.price}, {self.spec})'

