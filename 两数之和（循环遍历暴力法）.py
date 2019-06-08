'''给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的
那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
'''

def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if target-nums[i]==nums[j]:
                    return [i,j]
        return None
