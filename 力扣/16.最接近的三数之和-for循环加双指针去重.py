def threeSumClosest(nums, target):
    nums.sort()#排序，以便后续避免重复索引
    n=len(nums)
    res=nums[0]+nums[1]+nums[2]#预定一个输出，便于后续对比
    res_cha=abs(res-target)
    for k in range(n-2):
        i=k+1
        j=n-1
        while i<j:
            sum=nums[k]+nums[i]+nums[j]
            cha=sum-target
            if abs(cha)<res_cha:#绝对值进行对比
                res_cha=abs(cha)
                res=sum
            if cha>0:
                j-=1
                while i<j and nums[j]==nums[j+1]:j-=1#去重
            elif cha<0:
                i+=1
                while i<j and nums[i]==nums[i-1]:i+=1#去重
            else:
                return target#输出最接近target的数
    
    return res

nums=[0,1,2]
target=3
print(threeSumClosest(nums, target))