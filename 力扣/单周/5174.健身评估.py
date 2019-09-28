calories = [6,13,8,7,10,1,12,11]
n=len(calories)
lower=5
upper=37
s=0
k=6
for i in range(0,n,k):
	count=0
	for j in range(i,i+k):
		if j<n:
			count+=calories[j]
	print(count)
	if count<lower:
		s-=1
	elif count>upper:
		s+=1
print(s)