#multiple inhertance
class A:
    var1 = "welcome A"

class B:
    var2 = "welcome B"

class C(A,B):
    var3 = "welcome c"

c1 = C()

print(c1.var1)
print(c1.var2)
print(c1.var3)    
    