def threeSum(nums):
    #一个k的for循环，i、j从两端往中间逼近的双指针
    nums.sort()#排序，便于去重
    n=len(nums)
    res=[]
    for k in range(n-2):#k遍历
        if nums[k]>0: break # becaues of j>i>K
        if k>0 and nums[k]==nums[k-1]:continue #去重，取相等元素的第一个，取过的数不再取
        #若是取相等元素的最后一个，会影响i的取值
        i=k+1
        j=n-1
        while i<j:
            sum=nums[i]+nums[j]+nums[k]
            if sum<0:
                i+=1
                while i<j and nums[i]==nums[i-1]:i+=1#去重，取过的数不再取
            elif sum>0:
                j-=1
                while i<j and nums[j]==nums[j+1]:j-=1#去重，取过的数不再取
            else:
                res.append([nums[k],nums[i],nums[j]])#符合条件，添加到输出列表中
                i+=1#注意此时需要移动指针，不然会死循环
                j-=1#而且两个指针都要移动，去重
                while i<j and nums[i]==nums[i-1]:i+=1#作用同上
                while i<j and nums[j]==nums[j]+1:j-=1
                    
    return res

nums=[-1, 0, 1, 2, -1, -4]
print(threeSum(nums))