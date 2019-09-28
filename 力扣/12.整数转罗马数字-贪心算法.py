#贪心算法，在表示一个较大整数的时候，“罗马数字”不会让你都用 11 加起来，
#肯定是写出来的“罗马数字”的个数越少越好。
#类似找零钱
def intTOrome(num):
    # 把阿拉伯数字与罗马数字可能出现的所有情况和对应关系，放在两个数组中
    #此时不适合用字典，索引不方便
    # 并且按照阿拉伯数字的大小降序排列，这是贪心选择思想
    nums=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    romes=['M','CM','D','CD','C','XC','L','XL','x','IX','V','IV','I']
    n=len(nums)
    res=''
    index=0
    while index<n:#不超过数组的长度
        while num>=nums[index]:# 注意：这里是等于号，表示尽量使用大的"面值"
            res+=romes[index]
            num-=nums[index]
        index+=1
    return res

num=3
print(intTOrome(num))