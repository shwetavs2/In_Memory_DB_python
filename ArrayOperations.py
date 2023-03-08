class ArrayOperations:
    """Specifies operations which are supported on array value in the database"""
    def __init__(self, array_list=[]):
        self.array_list = array_list

    def put(self, value):
        if value == None or value == "":
            raise Exception("value should not be none or empty")
        else:
            self.array_list.append(value)
        return self.array_list

    def length(self):
        return len(self.array_list)

    def get(self, index):
        if (0 <= index) and (index < len(self.array_list)):
            return self.array_list[index]
        else:
            raise Exception("index out of bound")

    def get_int(self, index) -> int:
        if (0 <= index) and (index < len(self.array_list)):
            return int(self.array_list[index])
        elif type(self.array_list[index]) != int:
            raise Exception("not an int type")
        else:
            raise Exception("array index out of bound")

    def get_double(self, index) -> float:
        if (0 <= index) and (index < len(self.array_list)):
            return float(self.array_list[index])
        elif type(self.array_list[index]) != float:
            raise Exception("not an float type")
        else:
            raise Exception("array index out of bound")

    def get_string(self, index) -> str:
        if (0 <= index) and (index < len(self.array_list)):
            return str(self.array_list[index])
        elif type(self.array_list[index]) != str:
            raise Exception("not an string type")
        else:
            raise Exception("array index out of bound")

    def get_array(self, index) -> list:
        if (0 <= index) and (index < len(self.array_list)):
            return list(self.array_list[index])
        elif type(self.array_list[index]) != list:
            raise Exception("not an list type")
        else:
            raise Exception("array index out of bound")

    def get_object(self, index) -> object:
        if (0 <= index) and (index < len(self.array_list)):
            return dict(self.array_list[index])
        elif type(self.array_list[index]) != object:
            raise Exception("not an object type")
        else:
            raise Exception("array index out of bound")

    def remove(self, index):
        if (0 <= index) and (index < len(self.array_list)):
            del self.array_list[index]
            return self.array_list
        else:
            return None

    def to_string(self):
        return ''.join(map(str, self.array_list))

    @staticmethod
    def from_string(input):
        if '[' or ',' in input:
            str_obj = ArrayOperations()
            for key, val in eval(input):
                str_obj.put(key, val)
        return str_obj
