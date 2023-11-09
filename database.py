import json


class Database:

    def __init__(self):
        self.dict = {}

    def set_value(self, key, val):
        self.dict.update({key: val})
        return True

    def get_value(self, key):
        if key in self.dict.keys():
            return self.dict[key]
        return None

    def delete_value(self, key):
        if key in self.dict.keys():
            return self.dict.pop(key)
        return None


class DictManager(Database):
    def __init__(self):
        super().__init__()

    def set_value(self, key, val):
        super().set_value(key, val)
        f = open("database.json", "w")
        json.dump(self.dict, f)

    def delete_value(self, key):
        super().delete_value(key)
        f = open("database.json", "w")
        json.dump(self.dict, f)



