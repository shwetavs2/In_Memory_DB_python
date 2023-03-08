class Memento:
    """memento class stores the state of the object in memento pattern """
    def __init__(self, state):
        self.state = state


class CareTaker:
    """caretaker object triggers the memento to store the originator’s state."""

    def __init__(self, originator):
        self._originator = originator
        self._mementos = []

    def create(self):
        memento = self._originator.get_memento()
        print(memento.state)
        return memento.state

    def restore(self, index):
        memento = self._mementos[index]
        print(memento.state)
        self._originator.memento(memento)
