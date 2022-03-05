from dog_door import DogDoor

class Remote:
    def __init__(self, door: DogDoor) -> None:
        self._door = door

    def press_button(self):
        print("Pressing the remote control button...")
        if self._door.is_open():
            self._door.close()
        else:
            self._door.open()