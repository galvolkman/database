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

    def __str__(self):
        return self.dict.__str__()


class DictManager(Database):
    def __init__(self):
        super().__init__()
        f = open("database.json", "r")
        self.dict = json.load(f)

    def set_value(self, key, val):
        super().set_value(key, val)
        f = open("database.json", "w")
        json.dump(self.dict, f)


    def delete_value(self, key):
        super().delete_value(key)
        f = open("database.json", "w")
        json.dump(self.dict, f)

def main1():
    mydb = Database()
    mydb.set_value("kuku", "123456")
    print(mydb.get_value("gal"))
    print(mydb.get_value("eli"))
    print(mydb)


def main2():
    mydb = DictManager()
    mydb.set_value("kuku2", "123456")
    mydb.set_value("gal", "123456")

    print(mydb.get_value("gal"))
    print(mydb.get_value("eli"))
    print(mydb)


if __name__ == "__main__":
    #main1()
    main2()
    #main3()