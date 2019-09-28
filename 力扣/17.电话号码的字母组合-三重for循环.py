'''
def letterCombinations(digits):
    n=len(digits)
    if n==0:
        return []
    ds={
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
            }
    if n==1:
        return ds[digits]
    res=ds[digits[0]]
    i=0#代表digits的下标
    while i <n-1:#对digits循环
        i+=1
        di=ds[digits[i]]
        #print(di)
        temp=[]
        m=len(res)#res的长度
        for j in res:#res循环
            for k in di:#di循环
                temp.append(j+k)#将每一个最新元素添加至临时列表中
        res=temp#更新输出列表
    
    return res
'''

def letterCombinations(digits):
    if not digits: return []
    ds={
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
            }

    res=['']
    for i in digits:
        res=[j+k for j in res for k in ds[i]]
    return res

digits='23333'
print(letterCombinations(digits))