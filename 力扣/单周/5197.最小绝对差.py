#5197.最小绝对差.py
arr = [4,2,1,3]
arr.sort()
minnum=arr[1]-arr[0]
res=[[arr[0],arr[1]]]
n=len(arr)
for i in range(1,n-1):
	j=i+1
	tmp=arr[j]-arr[i]
	if tmp==minnum:
		res.append([arr[i],arr[j]])
	elif tmp<minnum:
		minnum=tmp
		del res[:]
		res.append([arr[i],arr[j]])
print(res)