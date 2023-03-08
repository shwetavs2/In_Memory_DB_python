
class ObjectOperations:
    """Specifies the operations supported by the objects in the database"""

    def __init__(self,Object={}):
        self.Object = Object

    def put(self,key,value):
        if value == None or value == "":
            raise Exception("value should not be null")
        else:
            self.Object[key]=value
        return self.Object

    def get(self, key):
        if key not in self.Object:
            raise Exception("Key not in dictionary")
        else:
            return self.Object[key]

    def get_int(self,key) -> int:
        if type(self.Object[key]) !=int or key not in self.Object:
            raise Exception("not an integer present in DB")
        else:
            return self.Object[key]

    def get_string(self,key) -> str:
        if type(self.Object[key]) != str or key not in self.Object:
            raise Exception("not an integer present in DB")
        else:
            return self.Object[key]

    def get_array(self, key) -> list:
        if type(self.Object[key]) != list or key not in self.Object:
            raise Exception("not an array present in DB")
        else:
            return self.Object[key]

    def get_double(self,key) -> float:
        if type(self.Object[key]) != float or key not in self.Object:
            raise Exception("not an float present in DB")
        else:
            return self.Object[key]

    def get_object(self,key) -> object:
        if type(self.Object[key]) != object or key not in self.Object:
            raise Exception("not an object present in DB")
        else:
            return self.Object[key]

    def length(self):
        return len(self.Object)

    def remove(self, key):
        if key not in self.Object:
            return None
        else:
            return self.Object.pop(key,None)

    def to_string(self):
        return str(self.Object)

    @staticmethod
    def from_string(input):
        if  '{' or ',' in input:
            object_obj = ObjectOperations()
            for key,val in eval(input):
                object_obj.put(key,val)
        return object_obj

        
            
