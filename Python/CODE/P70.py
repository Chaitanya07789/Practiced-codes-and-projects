class Student: 
    collage_name = "ABC"

    def __init__(self,name,age):
        self.name = name
        self.age = age
     
    def hello(self):
        print("hello",self.name)
        return self.age
          

s2 = Student("Ram",25)

print(s2.hello())
