#请在...补充一行或多行代码
#CalStatisticsV1.py
def getNum():       #获取用户不定长度的输入
    num=[]
    numstr=input('请输入数字（回车退出）：')
    while numstr!='':
        num+=numstr
        numstr=input('请输入数字（回车退出）：')
    return num
        
def mean(numbers):  #计算平均值
    s=0.0
    for i in numbers:
        s+=eval(i)
    return s/(len(numbers))
    
def dev(numbers, mean): #计算标准差
    s=0.0
    for i in numbers:
        s+=(eval(i)-mean)**2
    return pow(s/(len(numbers)-1),0.5)
        
def median(numbers):    #计算中位数
    m=len(numbers)//2
    numbers.sort()
    #对数列排序并返回到原数列，sorted(list)对数列排序并返回一个新序列
    if len(numbers)%2==0:
        return (numbers[m-1]+numbers[m])/2
    else:
        return numbers[m]
    
n =  getNum() #主体函数
m =  mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m,dev(n,m),median(n)))
