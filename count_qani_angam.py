class Person():
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.count += 1
obj = Person("Ashot", 22)
print(obj.count)
ob = Person("Ashot", 22)
print(ob.count)