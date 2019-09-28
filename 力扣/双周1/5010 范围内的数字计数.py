count=0
for i in range(low,high+1):
    i1=str(i)
    for j in range(len(i1)):
        if str(d) == i1[j]:
            count+=1
return count

'''
count=0
for i in range(low,hihg+1):
    i1=str(i)
    count+=i1.count(d)
return count
'''

#两个方法都超时了
