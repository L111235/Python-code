import turtle as t
t.setup(600,600,300,200)
#绘图框的宽、高，绘图框距屏幕左上角的左右、上下间距
t.width(2)
t.color('black')
k=360
for i in range(4):
    k-=90
    t.seth(k)
    
    '''以上代码可改写为：
k=270
for i in range(4):
    t.seth(k-90*i)
    
#i从0开始（如果seth函数的参数中存在‘=’会提示语法错误'''
    
    '''seth函数设置绝对坐标方向，只用设置每次循环开始时海龟的初始方向，不用管
每次循环结束时海龟的朝向'''
    
#用三个'作注释插入循环语句中时，句首需要缩进相应单位的空格
    t.fd(150)
    t.left(-90)
    #圆弧与当前朝向相切
    t.circle(-150,360/8)
    t.left(-90)
    t.fd(150)
    #上面两行代码可改写为t.goto(0,0)
    
t.done()
