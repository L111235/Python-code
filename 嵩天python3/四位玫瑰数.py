#test4.1.py
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            for n in range(10):
                if i**4+j**4+k**4+n**4==1000*i+100*j+10*k+n:
                    print('{}{}{}{}'.format(i,j,k,n))


'''
s = ""
for i in range(1000, 10000):
    t = str(i)
    if pow(eval(t[0]),4) + pow(eval(t[1]),4) + pow(eval(t[2]),4)+pow(eval(t[3]),4) == i :
        s += "{},".format(i)
print(s[:-1])
'''
