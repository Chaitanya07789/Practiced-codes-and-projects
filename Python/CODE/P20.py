print("Enter 3 numbers : ")
a = int(input())
b = int(input())
c = int(input())

if(a>=b and a>=c):
    print(a,"is a greatest of 3 number")
elif(b>=a and b>=c):
    print(b,"is a greatest of 3 number")
else:
    print(c,"is a greatest of 3 number")