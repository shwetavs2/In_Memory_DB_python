# In_Memory_DB_python
created a mini-in-memory database. NoSQL databases tend to act like hashtables. Each piece of data has a key. When you add data to the database, you provide the key and the data. To retrieve the data, you use the key. We will use strings as keys to keep things on the simple side. Our data will be Strings,Numbers, “Arrays” and “Objects.” “Arrays” are ordered lists of data (Strings, Numbers,“Arrays”, or “Objects”). A single “Array” can hold multiple types of data at the same time. An “Object” is a hashtable with a String as a key and any data as the value. You will find the JSON
library useful here. The operations on your NoSQL database will be to add new data, get the data at a given key, replace data at a given key, and remove a key and its data. Modifying data can be done with a retrieval and an add. Your first task is to implement the mini-in-memory database.

Array Operations
Your array needs at least the following methods.
put 
getX(int index)
get(int index)
length()
toString()
remove(int index)
class method: fromString- Has one argument of type string. The input is a string representation of an array. Returns at
array object created from the string. Throws an exception if the string does not represent a valid array object.

Object Operations
Your object needs at least the following operations.
put(String key, Y value)
getX(String key)
get(String key)
length()
remove(String key)
toString()
class method: fromString

DB Operations
Your database has to support the following basic operations.
put(String key, Y value)
getX(String key)
get(String key)
remove(String key)

Transactions
We need our database to support transactions. The database needs a transaction method that creates a transaction object and returns it. Each transaction on the database is independent of the other transactions on the database. We do not have to lock the Transaction object. Have the following basic methods:
put(String key, Y value)
getX(String key)
get(String key)
remove(String key)
commit()
abort()
isActive()

Persistence
The problem with in-memory data is that it is not persistent. So when the program stops running, the data is lost. For persistence, we will use two files. The first file, "commands.txt”, will contain all the operations done on the database that change
its state. The file will contain text, not binary. Each operation will be on a separate line. The operation needs to be saved to the file when the operation is being performed, preferably just before the operation is done.The second file, "dbSnapshot.txt” will contain the snapshot of the database. When a snapshot of the database is taken, the current data in the database is saved to this file. The previous contents of this file are removed. Also, the contents of the file “commands.txt” are removed.
The database needs four methods related to snapshots:
snapshot()
snapshot(File commands, File snapshot)
Class methods:
recover()
recover(File commands, File snapshot)

Reactive
Since the database is in memory, it does not have to be separate from an application like SQLite. So we could get some data and use it in the program. If the data in the database changes, we want our program to reflect the current state of the database. For this, we will add more methods to the database class.
getCursor(String key)

Cursor
A cursor holds a value from the database. The cursor knows the current state of the value. When the value changes in the database, the cursor knows the new state of the value. The cursor class needs the following methods:
getX()
get()
addObserver(Observer o)
removeObserver(Observer o)
