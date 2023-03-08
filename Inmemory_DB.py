

from ArrayOperations import ArrayOperations
from Objectoperations import ObjectOperations
from Transactions import Transaction
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from ObserverInterface import *
from ObservableInterface import *
from cursor import Cursor
from memento import *


@dataclass
class DbOperations:

    """provides support to the in-memory database for various operations including memento pattern"""

    command_file = "commands.txt"
    db_file = "db_snapshot.txt"

    def __init__(self, DB={}):
        self.DB = DB
        self._state = ""


    def put(self, key, value):
        self.set_state(f"Put {value} at {key}")
        caretaker_obj = CareTaker(db_object)
        obj = caretaker_obj.create()
        with open("commands.txt", "w") as file:
           file.write(str(obj))

        self.DB[key] = value
        return self.DB
        self.update()

    def get(self, key):
        if key not in self.DB:
            raise Exception("Key not in dictionary")
        else:
            return self.DB[key]

    def get_int(self, key) -> int:
        if type(self.DB[key]) != int or key not in self.DB:
            raise Exception("not an integer present in DB")
        else:
            return self.DB[key]

    def get_string(self, key) -> str:
        if type(self.DB[key]) != str or key not in self.DB:
            raise Exception("not an integer present in DB")
        else:
            return self.DB[key]

    def get_array(self, key) -> list:
        if type(self.DB[key]) != list or key not in self.DB:
            raise Exception("not an integer present in DB")
        else:
            return self.DB[key]

    def get_double(self, key) -> float:
        if type(self.DB[key]) != float or key not in self.DB:
            raise Exception("not an integer present in DB")
        else:
            return self.DB[key]

    def get_object(self, key) -> object:
        if type(self.DB[key]) != object or key not in self.DB:
            raise Exception("not an integer present in DB")
        else:
            return self.DB[key]

    def remove(self, key):
        self.set_state(f"Remove {key} from {self.DB[key]}")
        Caretaker_obj = CareTaker(db_object)
        obj = Caretaker_obj.create()
        file = open("commands.txt\n", "w")
        file.write(str(obj))

        if key not in self.DB:
            return None
        else:
            return self.DB.pop(key, None)

    def get_cursor(self, key):

        if key not in self.DB:
            raise Exception("Key not in db")
        else:
            return Cursor(key, db_object.DB)

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def get_memento(self):
        return Memento(self._state)

    def memento(self, memento):
        self._state = memento.state

    def snapshot(self,command_file,db_file):
        memento = self.get_memento()
        with open(db_file, "w") as file:
            file.writelines(str(db_object.DB) + "\n")
            pass

    def restore(self,command_file,db_file):
        with open("db_snapshot.txt", "r") as file:
            read_file = file.read()
        self.DB = eval(read_file)
        with open(command_file, "r") as file:
            command_file = file.readline()
            list1=[]
            list1.append(command_file.split(" "))

        for i in list1:
            key=i[2]
            value = i[1]
            Operation = i[0]
        if Operation == "Put":
            db_object.put(key, value)
        elif Operation== "Remove":
            db_object.remove(key)
            pass


class ObserverA(IObserver):
    """Observer class for objects"""

    def update(self, message) -> None:
        print("Observer: Reacted to the event", message)
        return


@dataclass()
class PutCommand:
    """Command class for database put method"""
    db: DbOperations
    key: object
    value: object

    def execute(self):
        return self.db.put(self.key, self.value)

    def undo(self):
        self.db.remove(self.key)


@dataclass
class RemoveCommand(DbOperations):
    """Command class for database remove method"""
    db: DbOperations
    key: str

    def execute(self):
        self.db.remove(self.key)

    def undo(self):
        self.db.put(self, self.key, self.value)


@dataclass
class TransactionController:
    """Controller for handling transactions done on database"""

    undo_stack: list[Transaction] = field(default_factory=list)
    active = True

    def execute(self, transaction: Transaction) -> None:
        transaction.execute()
        self.undo_stack.append(transaction)

    def undo(self) -> None:
        if not self.undo_stack:
            return
        for i in undo_stack:
            i.undo()

    def put(self, key, value):
        self.DB[key] = value
        return self.DB

    def get(self, key):
        if key not in self.DB:
            raise Exception("Key not in dictionary")
        else:
            return self.DB[key]

    def get_int(self, key) -> int:
        if type(self.DB[key]) != int or key not in self.DB:
            raise Exception("not an integer present in DB")
        else:
            return self.DB[key]

    def get_string(self, key) -> str:
        if type(self.DB[key]) != str or key not in self.DB:
            raise Exception("not an integer present in DB")
        else:
            return self.DB[key]

    def get_array(self, key) -> list:
        if type(self.DB[key]) != list or key not in self.DB:
            raise Exception("not an integer present in DB")
        else:
            return self.DB[key]

    def get_double(self, key) -> float:
        if type(self.DB[key]) != float or key not in self.DB:
            raise Exception("not an integer present in DB")
        else:
            return self.DB[key]

    def get_object(self, key) -> object:
        if type(self.DB[key]) != object or key not in self.DB:
            raise Exception("not an integer present in DB")
        else:
            return self.DB[key]

    def remove(self, key):
        if key not in self.DB:
            return None
        else:
            return self.DB.pop(key, None)

    def commit(self):
        self.undo_stack = []
        active = False

    def abort(self):
        for i in self.undo_stack:
            i.undo()
            active = False

    def isActive(self):
        return active


if __name__ == '__main__':
    db_object = DbOperations()
    # command pattern implementation for transactions
    db_object.put("age", 21)
    controller = TransactionController()
    controller.execute(PutCommand(db_object, "Name","Roger"))
    controller.abort()

    #Inmemeory database operations
    db_object.put("array",[1,2,3,4])
    db_object.put(1,2)
    db_object.put('account 12345', {"name":"Bill", "address":"123 main street", "phones":["619-594-3535"],"balance": 1234.05})
    db_object.remove(1)
    db_object.get("array")

    # Array operations
    array_object = ArrayOperations()
    array_object.put(1.2)
    array_object.put([1, 2, 3])
    array_object.put({"1": 2})
    db_object.put("key5",array_object.array_list)
    array_object.length()

    #memento pattern operations
    db_object.put("new", 1)
    db_object.snapshot(command_file="commands.txt",db_file="db_snapshot.txt")
    db_object.restore(command_file="commands.txt",db_file="db_snapshot.txt")

   #cursor object operations
    db_object.put("shweta",30)
    cursor_object=Cursor("shweta",db_object.DB)
    cursor_object=db_object.get_cursor("shweta")
    cursor_object.get("shweta")
    cursor_object.add_observer(ObserverA)
    cursor_object.update("shweta is changed")

