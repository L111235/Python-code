# encoding:utf-8
#5205.独一无二的出现次数
arr=[1,2]
dic={}
for i in arr:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
list1=[]
for key in dic:
    list1.append(dic[key])
list2=list(set(list1))
if len(dic)==len(list2):
    print('True')
else:
    print('False')