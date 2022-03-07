from dog_door import DogDoor
from bark import Bark
from remote import Remote
from bark_recognizer import BarkRecognizer

import time

def test_dog_door():
    '''Implements the dog door simulation

    (15 tests in total: 15 passed and 0 failed)
    
    
    >>> door = DogDoor()
    >>> door is not None
    True
    >>> door.get_allowed_barks() == [] #empty list
    True
    >>> door.add_allowed_bark(Bark('rowlf')) #append
    >>> door.add_allowed_bark(Bark('rooowlf'))
    >>> door.add_allowed_bark(Bark('rawlf'))
    >>> door.add_allowed_bark(Bark('woof'))
    >>> len(door._allowed_barks) == 4
    True
    >>> remote = Remote(door)
    >>> recognizer = BarkRecognizer(door)
    >>> print("Fido starts barking")
    Fido starts barking
    >>> recognizer.recognize(Bark("rowlf")) #True since it's a match
    BarkRecognizer: Heard a rowlf
    The dog door opens.
    True
    >>> print("Fido has gone out....")
    Fido has gone out....
    >>> recognizer.recognize(Bark("rooowlf")) #True since 'roowlf' has been appended earlier
    BarkRecognizer: Heard a rooowlf
    The dog door opens.
    True
    >>> print("Fido back in")
    Fido back in
    
    '''
    door = DogDoor()
    door.add_allowed_bark(Bark('rowlf'))
    door.add_allowed_bark(Bark('rooowlf'))
    door.add_allowed_bark(Bark('rawlf'))
    door.add_allowed_bark(Bark('woof'))

    remote = Remote(door)

    recognizer = BarkRecognizer(door)


    print("Fido starts barking")
    recognizer.recognize(Bark("rowlf"))
    print("Fido has gone out....")

    time.sleep(10)

    small_dog_bark = Bark("yip")

    recognizer.recognize(small_dog_bark)

    time.sleep(10)
    recognizer.recognize(Bark("rooowlf"))

    print("Fido back in")


if __name__ == "__main__":
    import doctest
    doctest.testmod()