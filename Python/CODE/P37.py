loop = (1,4,9,16,25,36,49,64,81,100)
i=0
val = False
num = int(input("enter value : "))
while i<len(loop):
    if(num == loop[i]):
        print(num,"is present and index is",i)
        val=True
    i += 1

if(val==False):
    print(num,"is not present")