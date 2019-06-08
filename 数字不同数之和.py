N=input()
set1=set(N)#去掉字符串（或者其它序列）中的重复元素
sum1=0
for i in set1:
    sum1+=eval(i)
print(sum1)
