# Inheritance // car & toyoyacar is single inheritance and car --> toyoyacar --> lamdo is multi-level inhertance
class Car:
    @staticmethod
    def star():
        print("stared")

    @staticmethod
    def stop():
        print("stopped")


class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name


class lambo(ToyotaCar):
    def __init__(self,type):
        self.tpye = type

# car1 = ToyotaCar("jbkasf")
# car2 = ToyotaCar("jbkmzncjzg")

car1 = lambo("racing")

print(car1.star())
