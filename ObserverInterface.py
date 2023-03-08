from abc import ABC, abstractmethod


class IObserver(ABC):
    """ The Observer interface declares the update method, used by subjects."""

    @abstractmethod
    def update(self, message):
        """Update observer state. """
