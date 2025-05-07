class Complex:
    def __init__(self, real_num, img_num):
        self.real_num = real_num
        self.img_num = img_num

    def showNumber(self):
        print(f"{self.real_num}i + {self.img_num}j")

    def __add__(self, num2):
        new_real = self.real_num + num2.real_num
        new_img = self.img_num + num2.img_num
        return Complex(new_real, new_img)
    
    def __sub__(self, num2):
        new_real = self.real_num - num2.real_num
        new_img = self.img_num - num2.img_num
        return Complex(new_real, new_img)



num1 = Complex(2, 4)
num1.showNumber()

num2 = Complex(5, 7)
num2.showNumber()

num3 = num1 - num2
num3.showNumber()