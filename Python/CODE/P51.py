def fac(n):

    fact = 1
    # while i<=n:
    #     fact *= i
    #     i += 1
    for i in range(1,n+1):
        fact *= i
    return fact

n= int(input())
print(fac(n))