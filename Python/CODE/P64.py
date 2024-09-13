with open("practice.txt","r") as f:
    # f.write("hi everyone\nwe are learing file I/O\n")
    # f.write("using Java.\nI like programming in java")
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)