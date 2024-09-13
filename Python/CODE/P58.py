
f = open("D:\Python\CODE\demo.txt","rt")
data = f.readline()
print(data)

data1 = f.readline()
print(data1)

print(type(data))
f.close()