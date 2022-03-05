from bark import Bark

from threading import Timer


class DogDoor:
    def __init__(self):
        self.is_open = False
        self._allowed_barks = list()

    def add_allowed_bark(self, bark: Bark):
        self._allowed_barks.append(bark)

    def get_allowed_barks(self):
        return self._allowed_barks

    def open(self, close_door_time = 5):
        print("The dog door opens.")
        self.is_open = True
        
        door_close_on_timer = Timer(close_door_time, self.close).start()
        return
    
    def close(self):
        if self.is_open is True: #if door is open (Still)
            self.is_open = False
            print("The dog door closes")
        return
    
    def is_open(self):
        return self.is_open
