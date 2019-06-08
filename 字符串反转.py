#将字符串s反转后输出
#s[::-1] #按-1的步长选取字符串s的第一个字符到最后一个字符
s=input('请输入一个字符串:')
def rvs(s):
    if s=='':
        return s
    else:
        return rvs(s[1:])+s[0]

    #rvs(s[1:])=rvs(s[2:])+s[1],s=rvs(s[2:])+s[1]+s[0]
    #要在return后递归调用函数本身，return代表函数的输出（可以理解为一行新命令）

print(rvs(s))
#print(s)  #假如未调用rvs函数，则输出的s是原输入字符串（全局变量）
