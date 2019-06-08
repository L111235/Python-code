'''#test4.2.py
sum=5
a=0
for i in range(4,101):
    for j in range(2,i):
        if i%j==0:
            i=0
            break
    sum+=i
print(sum)'''

#Prime
def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
sum = 0
for i in range(2,100):
    if is_prime(i):
        sum += i
print(sum)
        
