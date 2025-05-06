class Student:
    # Constructor
    country = "Pakistan" # Class Attributes
    def __init__(self, name, marks):
        self.marks = marks # Object Attributes
        self.name = name
    # Methods
    def welcom(self):
        print(f"Hello {self.name}")

    def get_marks(self):
        return self.marks
    
    # Static Methods
    @staticmethod
    def say_hello():
        print(f"Hello, how are you")

s1 = Student("Zain", 76)
s1.say_hello()