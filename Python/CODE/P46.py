n= int(input('enter value : '))
i=1
sum =0
while i<=n:
    sum=i+sum
    i += 1
print(sum)

fact = 1
for i in range(1,n+1):
    fact = i * fact
print(fact)
