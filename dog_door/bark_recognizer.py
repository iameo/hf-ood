from bark import Bark
from dog_door import DogDoor

class BarkRecognizer:
    def __init__(self, door: DogDoor):
        self._door = door
        
    def recognize(self, bark: Bark):
        print(f"BarkRecognizer: Heard a {bark}")
        
        #for-else loop
        for allowed_bark in self._door.get_allowed_barks():
            if allowed_bark.equals(bark):
                self._door.open()
                return True
        else:
            print("This dog is not allowed.")
