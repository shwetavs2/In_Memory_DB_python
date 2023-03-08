from abc import ABC, abstractmethod


class Transaction(ABC):
    """Transaction class to handle the transactions , the interface has execute and undo abstract methods"""
    @abstractmethod
    def execute(self) -> None:
        """execute method"""

    @abstractmethod
    def undo(self) -> None:
        """undo method"""
