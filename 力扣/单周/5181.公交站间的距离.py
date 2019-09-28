distance=[7,10,1,12,11,14,5,0]
n=len(distance)
print(n)
start=7
destination=2
start_new=min(start,destination)
destination_new=max(start,destination)
sum1=0
sum2=0
for i in range(start_new,destination_new):
	sum1+=distance[i]
for j in range(start_new):
	sum2+=distance[j]
for k in range(destination_new,n):
	sum2+=distance[k]
res=min(sum1,sum2)
print(res)