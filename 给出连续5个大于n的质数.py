'''
def prime(m):
    end = int(pow(m, 0.5) + 1)
    for i in range(2, end):
        if m%i == 0:
            return False
    else:
        return True

n = eval(input())
if n != int(n):  # 因为可能输入有浮点数
    n = int(n) + 1
else:  # 保证输入5.0时，输出为整数5。这里只根据题目中只输入正浮点或者正整数时做的处理
    n = int(n)  
count = 5
while count > 0:
    if prime(n):
        if count > 1:
            print(n, end=',')
        else:
            print(n)
        count -= 1
    n += 1
'''





def prime(m):
    for i in (2,m**0.5):
        if m%i==0:
            return None
        else:
            return m

n = eval(input())
n=int(n)+1 if n!=int(n) else int(n) #注意：else后面不用写n=
count=0
while True:
    if prime(n)==None:
        n+=1
    elif count==4:
        print(prime(n))
        break
    else:
        print(prime(n),end=',')
        n+=1
        count+=1
