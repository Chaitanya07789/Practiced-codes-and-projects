class Car:
    def __init__(self,type):
        self.type= type
    @staticmethod
    def star():
        print("stared")

    @staticmethod
    def stop():
        print("stopped")


class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)

car1 = ToyotaCar("prius","electric")
print(car1.type)
