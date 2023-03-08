from ObservableInterface import *
from abc import ABC, abstractmethod


class Cursor(IObservable):
    """The cursor class object holds a value from the database and updates the observer if the values changes"""
    def __init__(self, key, db_object):
        self.db = db_object
        self.key = key
        self.value = self.db[key]
        self._observers = []

    def get(self, key):
        return self.db[key]

    def get_int(self, key) -> int:
        if type(self.DB[key]) != int or key not in self.DB:
            raise Exception("value not an integer")
        else:
            return self.DB[key]

    def get_string(self, key) -> str:
        if type(self.DB[key]) != str or key not in self.DB:
            raise Exception("value not string")
        else:
            return self.DB[key]

    def get_array(self, key) -> list:
        if type(self.DB[key]) != list or key not in self.DB:
            raise Exception("not an array")
        else:
            return self.DB[key]

    def get_double(self, key) -> float:
        if type(self.DB[key]) != float or key not in self.DB:
            raise Exception("not an float value")
        else:
            return self.DB[key]

    def get_object(self, key) -> object:
        if type(self.DB[key]) != object or key not in self.DB:
            raise Exception("value not an object")
        else:
            return self.DB[key]

    def add_observer(self, Observer):
        self._observers.append(Observer)
        return

    def remove_observer(self, Observer):
        self._observers.remove(Observer)
        return

    def update(self, message):
        for Observer in self._observers:
            Observer.update(self, message)
        return
