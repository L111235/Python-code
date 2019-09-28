def fourSum(nums, target) :
    #头尾两个k、m的for循环，i、j从两端往中间逼近的双指针
    nums.sort()#排序，便于去重
    n=len(nums)
    res=[]
    for k in range(n-3):#k遍历
        #print(nums[k])
        if k>0 and nums[k]==nums[k-1]:continue #去重，取相等元素的第一个，取过的数不再取
        for m in range(n-1,k+2,-1):
            #print(nums[m])
            if m<n-1 and nums[m]==nums[m+1]:continue#去重
            i=k+1
            #print(nums[i])
            j=m-1
            #print(nums[j])
            while i<j:
                sum=nums[i]+nums[j]+nums[k]+nums[m]
                cha=sum-target
                if cha<0:#和小了就加大一点
                    i+=1
                    while i<j and nums[i]==nums[i-1]:i+=1#去重，取过的数不再取
                elif cha>0:#和大了就减小一点
                    j-=1
                    while i<j and nums[j]==nums[j+1]:j-=1#去重，取过的数不再取
                else:
                    res.append([nums[k],nums[i],nums[j],nums[m]])#符合条件，添加到输出列表中
                    i+=1#注意此时需要移动指针，不然会死循环
                    j-=1#而且两个指针都要移动，去重
                    while i<j and nums[i]==nums[i-1]:i+=1#作用同上
                    while i<j and nums[j]==nums[j]+1:j-=1
                
    return res

nums=[-3,-1,0,2,4,5]
target=0
print(fourSum(nums, target))