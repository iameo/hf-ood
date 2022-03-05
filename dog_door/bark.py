
class Bark:
    def __init__(self, sound):
        self.sound = sound
        
    def get_sound(self):
        return self.sound
    
    def equals(self, other_bark):
        if not isinstance(other_bark, Bark):
            raise NotImplemented
        return True if self.sound.lower() == other_bark.sound.lower() else False
    
    def __repr__(self):
        return str(self.sound)