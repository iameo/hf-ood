from builder import Builder
from type_ import Type
from wood import Wood


class GuitarSpec:
    ''' class to represent a Guitar Spec Object'''
    def __init__(self, builder: Builder, model: str, stringNum: int, _type:Type, wood: Wood):
        self.builder = builder
        self.model = model
        self.stringNum = stringNum
        self._type = _type
        self.wood = wood

    def get_builder(self) -> Builder:
        return self.builder
    
    def get_model(self) -> str:
        return self.model
    
    def get_type(self) -> Type:
        return self.wood
    
    def get_wood(self) -> Wood:
        return self.wood
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.builder.value}, {self.model}, {self.stringNum}, {self._type.value}, {self.wood.value})'
