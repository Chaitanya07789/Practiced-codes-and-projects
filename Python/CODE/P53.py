def odd_even(n):
    a = None
    if(n%2==0):
        a ="even"
    else:
        a ="odd"
    return a

n = int(input())

print("number is ",odd_even(n))