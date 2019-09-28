
def maxArea(height):
    n=len(height)
    maxarea=0
    i=0
    for i in range(n-1):
        j=i+1
        while j<n:
        	maxarea=max(maxarea,(j-i)*min(height[j],height[i]))
        	j+=1
    return maxarea

height=[1,8,6,2,5,4,8,3,7]
print(maxArea(height))

