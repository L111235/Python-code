'''给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的
那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
'''

def twoSum( nums, target) :
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        lookup = {}   #建一个空字典
        
    #(1，2，3)代表tuple元组数据类型，元组是一种不可变序列。
    #['p', 'y', 't', 'h', 'o', 'n']代表list列表数据类型
    #{'lili': 'girl', 'jon': 'boy'}代表dict字典数据类型，字典是由键对值组组成
        
        for i in range(n):
            tmp = target - nums[i]  #tmp可以理解为nums[j]
            if tmp in lookup:       #判断nums[i]+nums[j]是否等于target
                return [lookup[tmp], i]
            lookup[nums[i]] = i  #在字典lookup里增加键为nums[i]、值为i的数据
'''
把nums[i]为键、i为值添加到字典lookup中，然后用后续的target-nums[i]与字典中的
nums[i]值进行对比，就可以把执行一个循环的时间变为一个数值与字典中的值进行对比
的时间

    
#列表中的元素或者字典中的键值可以是int数值
#假如nums中有两个相同元素2，2，且target是4的话，第一个tmp会保存在字典中，第二个
#会直接输出
'''
