N=eval(input())
M=N
i=1
while N>0:
    a='*'*i
    print('{0:^{1}}'.format(a,M))
    #槽{}内嵌套槽{}需要指定各个槽对应的format中的变量序号
    #print(a.center((M+1)//2))为什么这里用center函数不行
    N-=2
    i+=2
