# 请在...补充一行或多行代码
steps = 0
def hanoi(src, des, mid, n):
    global steps
    if n == 1:
        steps+=1  #递归链条每调用一次基例，steps都+1
        print("[STEP{:>4}] {}->{}".format(steps, src, des))
    else:  #当n大于1时：
        hanoi(src,mid,des,n-1)  #先将A上n-1个圆盘移到B上
        #根据递归的实现过程，第一次调用基例时转移的是最顶层的圆盘
        hanoi(src,des,mid,1)    #再将A上最底下一个圆盘移到C上
        #实际上
        hanoi(mid,des,src,n-1)  #再将B上n-1个圆盘移到C上
        
N = eval(input())
hanoi("A", "C", "B", N)
