loop = [4,5,6,7,8]
cities = ["delhi","pune","mumbai","noida","narhe"]

def length(list):
    count=0
    for val in list:
        count += 1
 
    return count
    
def print_len(list):
    print(len(list))

print_len(loop)
print_len(cities)
print(length(loop))


def print_list(list):
    for val in list:
        print(val,end=" ")

print_list(cities)