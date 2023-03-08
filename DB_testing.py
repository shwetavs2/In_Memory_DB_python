import os.path
import unittest
from Inmem import DbOperations
from ArrayOperations import ArrayOperations
from Objectoperations import ObjectOperations


class TestCase(unittest.TestCase):

    def test_db(self):
        database_obj = DbOperations({})
        value = database_obj.put('1', 'value1')
        self.assertEqual(value, {'1': 'value1'})
        self.assertEqual(database_obj.get('1'), "value1")

    def test_array_file(self):
        database_obj = DbOperations({})
        object_operations_object = ObjectOperations({})
        array_obj = ArrayOperations()
        array_value = array_obj.put(2)
        database_obj.put("2", [1])
        self.assertEqual(array_value, [2])
        self.assertEqual((database_obj.put("2", array_value)), {"2": [2]})
        self.assertEqual(array_obj.length(), 1)
        self.assertEqual(object_operations_object.put("obj", 2.4), {"obj": 2.4})
        self.assertEqual(object_operations_object.get_double("obj"), 2.4)
        database_obj.snapshot()
        self.assertEqual(True, os.path.exists("db_snapshot.txt"))


if __name__ == '__main__':
    unittest.main()
