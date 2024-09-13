class Stu:
    def __init__(self,name,passw):
        self.name = name
        self.__passw = passw

    def reset_pas(self):
        print(self.__passw)

s1 = Stu("Ram","abchvjh")
print(s1.name)
print(s1.reset_pas())
# del s1.name
print(s1.__passw) #error