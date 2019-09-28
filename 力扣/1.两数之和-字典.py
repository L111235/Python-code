#两数之和.py
#建立字典dict，把target-nums[i]:i依次存入字典中，并同时与nums[i]对比
def twosum(nums,target):
	n=len(nums)
	dict2={}
	for i in range(n):
		if nums[i] in dict2:#将指针当前对应的值与字典中的差值对比
			return [dict2.get(nums[i]),i]#差值（键）对应的下标（值）与当前下标i
		else:
			temp=target-nums[i]#差值作为键
			dict2[temp]=i#下标作为值

nums=[2,7,11,15]
target=9
print(twosum(nums,target))

