def romanToInt(s):
    ri={'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}

    i=0
    n=len(s)
    res=0
    while i<n:
        if i==n-1:#当i==n-1时，不能在用下述判断，不然会超过字符串s范围
            res+=ri[s[i]]
            i+=1
            break
        if ri[s[i]]>=ri[s[i+1]]:#i+1不能超过s的最大索引值n-1
            res+=ri[s[i]]
            i+=1#使用一个元素就加一位
        else:
            res+=ri[s[i:i+2]]
            i+=2#用用两个元素就加两位
            
    return res
#也可以用一个for循环一个一个加，如果前一个小于后一个，那就是加它的负数
#最后一个字符要单独加，不能进行比较

s="MCMXCIV"
print(romanToInt(s))