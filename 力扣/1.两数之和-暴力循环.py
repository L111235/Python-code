#两数之和.py
def twosum(num,target):
	n=len(nums)
	for i in range(n-1):
		for j in range(i+1,n):
			if target-nums[i]==nums[j]:
				return [i,j]

nums=[2,7,11,15]
target=9
print(twosum(nums,target))