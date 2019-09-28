
f=open('latex.log','r')
count=0
for line in f.readlines():
    line=line.strip('\n')
    if len(line) !=0:
        count+=1
        print(line)
print('共{}行'.format(count))
'''空格也算字符'''
'''
f = open("latex.log")
s = 0
for line in f:
    line = line.strip('\n')
    if len(line) == 0:
        continue
    s += 1
print("共{}行".format(s))
'''