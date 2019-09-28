#5173.质数排列
n=100
num=2
i=2
s=0
for i in range(2,n+1):
	for num in range(2,i):
		if (i%num==0):
			break
	else:
		s+=1
print(s)
count=1
count1=1
for j in range(1,s+1):
	count=count*j
for k in range(1,n-s+1):
	count1=count1*k
count=count*count1
count=count%(pow(10,9)+7)
print(count)
#5 ,11, 100