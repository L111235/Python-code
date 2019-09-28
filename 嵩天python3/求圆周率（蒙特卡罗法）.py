#CalpiV2.py
from time import perf_counter
from random import random
DARTS=1000*1000
#DARTS=1000*1000*10
hits=0.0
start=perf_counter()
#for i in range(DARTS):
for i in range(1,1+DARTS):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)#求点（x,y）到原点的距离
    if dist<=1.0:
        hits+=1
pi=4*(hits/DARTS)
print("圆周率为：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter()-start))
