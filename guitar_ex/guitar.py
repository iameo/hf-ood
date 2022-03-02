from guitarspec import GuitarSpec

class Guitar:
    ''' The Guitar class for making guitar instances with the details'''
    def __init__(self, serialNum: str, price: float, spec: GuitarSpec):
        self.serialNum = serialNum
        self.price = price
        self.spec = spec
        
        
    def get_spec(self) -> GuitarSpec:
        ''' return the guitar spec'''
        return self.spec
    
    def _match_by_spec(self, other: GuitarSpec):
        '''compare two guitarspec objects, check for same guitarspec'''
        _guitarspec = self.get_spec()
        
        return True if (
            _guitarspec.get_builder() == other.get_builder() and _guitarspec.get_model() == other.get_model() \
                and _guitarspec.get_type() == other.get_type() and _guitarspec.get_wood() == other.get_wood()) else False

    def __repr__(self):
        return f'{self.__class__.__name__}({self.serialNum}, {self.price}, {self.spec})'
        