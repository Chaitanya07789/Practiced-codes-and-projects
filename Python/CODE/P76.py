class Person:
    __name = "no"

    def __hello(self):
        print("hello")

    def welcom(self):
        self.__hello()

p1 = Person()

print(p1.welcom())
print(p1.__hello()) #error