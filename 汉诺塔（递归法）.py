#hanoi
'''
利用一个中间柱子，将第一个柱子上的圆盘转移到第三个柱子上
且小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘
'''
count=0
def hanoi (n,src,dst,mid):
    global count
    if n==1:
        print('{}:{}->{}'.format(1,src,dst))
        count+=1
    else :
        hanoi(n-1,src,mid,dst) #将最上面的n-1个圆盘从初始位移动到过渡位
        print('{}:{}->{}'.format(n,src,dst))  #n代表第n个圆盘
        #将初始位的最底下的一个圆盘移动到目标位
        count+=1
        hanoi(n-1,mid,dst,src)
        #将过渡位的n-1个圆盘移动到目标位

hanoi(2,'A','C','B')
print(count)
