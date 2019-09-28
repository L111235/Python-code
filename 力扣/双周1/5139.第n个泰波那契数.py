'''递归：
def tribonacci(n):
if n==0:
    return 0
elif n==1:
    return 1
elif n==2:
    return 1
else:
    res=tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
    if res<(pow(2,31)-1):
        return res 
    else:
        return pow(2,31)-1
'''

#循环代替递归（优选）
def tribonacci(n):
    res={}
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        i=3
        res[0]=0
        res[1]=1
        res[2]=1
        while i<=n:
            res[i]=res[i-1]+res[i-2]+res[i-3]
            i+=1
        if res[n]<(pow(2,31)-1):
            return res[n] 
        else:
            return pow(2,31)-1

n=29
print(tribonacci(n))
