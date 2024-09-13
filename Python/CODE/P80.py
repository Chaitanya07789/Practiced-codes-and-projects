# for chnging class attributes
class Person:
    name = "no"

    # def changename(self,name):
    #     self.__class__.name=name
    #     #Person.name = name

    @classmethod
    def changename(cls,name):
        cls.name= name

p1 = Person()
p1.changename("ram")
print(p1.name)
print(Person.name)