#Cal n!
n=eval(input('请输入一个不小于0的整数:'))
def jc(n):
    if n==0:
        return 1
    else:
        return n*jc(n-1)  #用一个新的内存来存储n-1的函数
print(jc(n))
