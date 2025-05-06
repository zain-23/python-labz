class Student:
    def __init__(self, math, physics, chemistry):
        self.math = math
        self.physics = physics
        self.chemistry = chemistry
    
    @property
    def percentage(self):
        return str((self.math + self.physics + self.chemistry) / 3) + "%"

zain = Student(89, 89, 95)
print(zain.percentage)
zain.physics = 50
print(zain.percentage)
