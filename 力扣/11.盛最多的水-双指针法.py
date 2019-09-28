'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
'''
#双指针法
def maxArea(height):
	#双指针法：短线段不变, 长线段向内收缩的话，无论之后的线段再长，
	#也要以短线段长度为基准，但两条线段之间的距离却缩短了，
	#所以不可能比之前装的水多
    maxarea=0
    i=0
    j=len(height)-1

    while i<j:
    	if height[i]<height[j]:
    		maxarea=max(maxarea,(j-i)*height[i])
    		i+=1
    	else:
    		maxarea=max(maxarea,(j-i)*height[j])
    		j-=1
    return maxarea

height=[1,8,6,2,5,4,8,3,7]
print(maxArea(height))