log=open('latex-1.log')
cs=0
d={}
'''for i in range(26):
    d[chr(ord('a')+i)]=0
#将26个小写字母都放到字典里面，值均为0
'''
for line in log:
    for i in line:
        d[i]=d.get(i,0)+1
        cs+=1
#字符不一定都是小写字母
print('共{}字符'.format(cs),end='')
for i in range(26):
    if d.get(chr(ord('a')+i),0)!=0:
        print(',{}:{}'.format(chr(ord('a')+i),d[chr(ord('a')+i)]),end='')
#假如其中一个小写字母没有出现过，那么它作为键对应的值就不存在