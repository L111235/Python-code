import jieba
import time
txt=open('沉默的羔羊.txt','r',encoding='utf-8')
list_txt=jieba.lcut(txt.read())
counts={}
start=time.time()
for i in list_txt:
    if len(i)>1:
        counts[i]=counts.get(i,0)+1
t=time.time()-start
print(t)
maxcount=0
maxword=''
start=time.time()
for i in counts:
    if counts[i]>maxcount and len(i)>1:
        maxcount=counts[i]
        maxword=i
    if counts[i]==maxcount and len(i)>1 and i>maxword:
        maxword=i
'''
start=time.time()
items=list(counts.items())
items.sort(key=lambda x:(x[1],x[0]),reverse=True)
'''
t=time.time()-start
print(t)
print(items[0][0])
txt.close()