from abc import ABC, abstractmethod


class IObservable(ABC):
    """ The Observable interface declares a set of methods for managing observers."""

    @abstractmethod
    def add_observer(self, observer):
        """add an observer"""

    @abstractmethod
    def remove_observer(self, observer):
        """remove an observer"""

    @abstractmethod
    def update(self, message):
        """update a message to method"""
