def print_ele(list,index):
    if(index == len(list)):
        return
    print(list[index],end=" ")
    print_ele(list,index+1)
    
    
list = [1,2,3,4,5,6,7,8,9]
print_ele(list ,0)