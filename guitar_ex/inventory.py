from guitar import Guitar
from guitarspec import GuitarSpec 


class Inventory:
    '''Inventory class to hold guitars'''
    def __init__(self):
        self._guitars = list()
        
    def add_guitar(self, guitar: Guitar):
        self._guitars.append(guitar)
        return
    
    def search(self, guitar: GuitarSpec) -> list:
        similar_guitars = list()
        
        for _guitar in self._guitars:
            if not _guitar._match_by_spec(guitar):
                continue
            similar_guitars.append(_guitar)

        return similar_guitars
    
    @property
    def guitars(self):
        return self._guitars