import time
scale=50
print('执行开始'.center(scale//2,'-'))

#执行开始置于中间，左右两侧用-补齐
#不能是50/2（这个会输出带小数的浮点数），//表示求商取整。

start=time.perf_counter()

#获取当前cpu时间（随机时间，只有两个时间段的差值才有意义）

for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    #i占scale的百分比例
    dur=time.perf_counter()-start
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end='')
    # ^表示居中对齐，百分比进度长度保持为3取整.0f，时间取小数点后两位.2f
    time.sleep(0.1)
print('\n执行结束'.center(scale//2,'-'))

#由于python的idle自动屏蔽了\r功能，因此要将此程序在cmd命令行中运行
#假如报错：unexpected EOF while parsing，意味着可能少了括号。parsing：语法分析 
