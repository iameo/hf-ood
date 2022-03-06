class InstrumentSpec:
    def __init__(self, properties: dict):
        self._properties = properties
    
    def get_property(self, property_name):
        return self._properties.get(property_name)
    
    def get_properties(self):
        return self._properties

    def _match(self, other):      
        for prop_name in other.get_properties():
            if prop_name not in self.get_properties():
                return False
            if self._properties[prop_name] != other.get_property(prop_name):
                return False
        return True
    
    def matches(self, other):
        if not isinstance(other, InstrumentSpec):
            raise TypeError(f'Expected {type(self)} got {type(other)}')
        return self._match(other)


    def __repr__(self):
        return f'{self.__class__.__name__}({self._properties})'