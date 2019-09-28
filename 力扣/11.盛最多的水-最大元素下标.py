
def maxArea(height):
    n=len(height)
    maxindex=height.index(max(height))  
    #找出列表中第一个最大元素对应的下标
    maxarea=0
    i=0
    while i<n-1 and i<maxindex+1:
        j=i+1
        while j<n:
        	maxarea=max(maxarea,(j-i)*min(height[j],height[i]))
        	j+=1
        while height[i]>=height[i+1] and i<maxindex:
             #由于下标为maxarea对应的值最大，因此i最多取到maxindex
            i+=1 
        i+=1
        #由于height[i+1]大于height[i]，所以取下标为i+1。最终i的值会取到maxindex+1为止
    return maxarea

height=[1,8,6,2,5,4,8,3,7]
print(maxArea(height))

