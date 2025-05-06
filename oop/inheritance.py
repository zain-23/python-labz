# Multi level inheritance
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started -->>>")

    @staticmethod
    def stop():
        print("Car stop -->>>")

class ToyotaCar(Car):
    def __init__(self, brand, type):
        self.brand = brand
        super().__init__(type)
        super().start()

# Multiple level inheritance
class A:
    var1 = "Syed"

class B:
    var2 = "Zain"

class C(A, B):
    var3 = "Ali"


class Bird:
    name = "Eagle"
    
    @classmethod
    def changeName(cls, name):
        cls.name = name

bird1 = Bird()

bird1.changeName("Pea cock")

print(bird1.name)
print(Bird.name)