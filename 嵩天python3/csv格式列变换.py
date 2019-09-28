f=open('data.csv')
for line in f.readlines():
    line=line.strip('\n')
    ls=line.split(',')
    #ls.reverse()
    ls=ls[::-1]
    line=','.join(ls)
    print(line)