'''
等价多米诺骨牌对的数量 

给你一个由一些多米诺骨牌组成的列表 dominoes。
如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。
形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。
在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。
'''

#核心思想：每个元素尽可能只用一次
def numEquivDominoPairs(dominoes) :
    n=len(dominoes)
    count=0
    res=0
    while n:
        j=1
        while j<n:
            if dominoes[0]==dominoes[j] or dominoes[0][::-1]==dominoes[j]:
                count+=1
                dominoes.pop(j)
                j-=1
            j+=1
            n=len(dominoes)#长度n要实时变化
        count+=1#要统计第1个元素
        dominoes.pop(0)#通过指定下标的方式移除已统计过的元素
        #dominoes=list(set(dominoes)-set(temp))#列表不能哈希
        n=len(dominoes)#长度n要实时变化
        res+=count*(count-1)/2#C(2,n)
        count=0
    return int(res)

dominoes = [[1,2],[2,1],[3,4],[5,6]]
print(numEquivDominoPairs(dominoes))