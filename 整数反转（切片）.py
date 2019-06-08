def reverse(x: int) -> int:
    if x>=0:
        x=int(str(x)[::-1])  #eval函数无法去掉x前面的0，比如120反转则为021
        #按步长为1从右往左切片，即按步长为-1切片
    else:
        x=0-int(str(x)[:0:-1])   #x=0-int(str(abs(x))[::-1])

    #按-1步长切片的话，第一个数代表字符串右侧位置，第二个数左侧，从右往左切片
    #而且还是左闭右开
        
    if -2147483648<=x<=2147483647:
        return x
    #else:   #这个else可以不用，因为假如前面一个情况成立，则返回x，函数结束
    return 0

x=int(input())
print(reverse(x))
