#14.最长公共前缀
#参考英语字典的排序方式，sort对字符串会依据unicode码排序
def longestCommonPrefix(s):
    if not s:
        return ""
    s.sort()
    print(s)
    n = len(s)
    a = s[0]
    b = s[n-1]
    res = ""
    for i in range(len(a)):
    #i=len(b)
        if  a[i] == b[i]: #and i < len(b):
        #i不能可能取到比b的长度还要大的值，不然b不可能排在a后面
        #i会在小于b的长度时就由于不满足条件而退出循环
            res += a[i]
        else:
            break
    return res


strs=["dog","ra","car"]
print(longestCommonPrefix(strs))
