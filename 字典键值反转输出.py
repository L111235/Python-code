#d={"a": 1, "b": 2}
d=eval(input())  #输入一个字典数据，input()函数返回值实际为为一个字符串
try:
    d1={}
    for i in d:
        #print(i)
        #value=d[i]
        d1[d[i]]=i
    print(d1)
except:
    print('输入错误')
