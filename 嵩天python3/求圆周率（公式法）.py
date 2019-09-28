#CalPiV1.py
from time import perf_counter
start=perf_counter()
#函数即使使用默认参数，也要加上()
pi=0
N=100
for k in range(N):
    '''pi+=1/pow(16,k)*(\
        4/(8*k+1)-2/(8*k+4)-\
        1/(8*k+5)-1/(8*k+6))'''
    pi+=1/(16**k)*(\
        4/(8*k+1)-2/(8*k+4)-\
        1/(8*k+5)-1/(8*k+6))
#\放于行尾代表换行输入
#print("运行时间为：{:.5f}s".format(perf_counter()-start))
print("圆周率是:{}".format(pi))
print("运行时间为：{:.5f}s".format(perf_counter()-start))

'''#CalPiV1.py
pi = 0
N = 100
for k in range(N):
    pi += 1/pow(16,k)*( \
              4/(8*k+1) - 2/(8*k+4) - \
              1/(8*k+5) - 1/(8*k+6) ) 
print("圆周率值是: {}".format(pi))'''
