#科赫雪花
import turtle as t
def koch(size,n):
    if n==0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)
            #n-1阶科赫曲线相当于0阶，n阶相当于1阶
            #用一阶图形替代0阶线段画二阶科赫曲线
            #用n-1阶图形替代0阶线段画n阶科赫曲线
            #将最小size的3倍长的线段替换为一阶科赫曲线
            #只画了第n阶的科赫曲线
            #每递归一次size都要除以3，初始n阶科赫曲线的size固定
def main():
    t.setup(800,800,200,20)
    t.width(2)
    t.penup()
    t.goto(-200,150)
    t.pendown()
    a=120
    for i in range(360//a):#对商取整，range函数参数必须为int型，不能是float
        koch(400,3)
        t.right(a)
    t.hideturtle()
    t.done
main()
