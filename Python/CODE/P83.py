# polymorphisum

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show_no(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newreal =self.real+num2.real
        newimg = self.img+num2.img
        return Complex(newreal,newimg)

    def __sub__(self,num2):
        newreal =self.real-num2.real
        newimg = self.img-num2.img
        return Complex(newreal,newimg)

num1=Complex(1,2)
num1.show_no()
num2=Complex(4,6)
num2.show_no()

num3=num1-num2
# num3 =num1+num2
# num3=num1.add(num2)
num3.show_no()