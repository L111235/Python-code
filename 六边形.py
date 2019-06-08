import turtle
turtle.setup(600,600,300,200)
#绘图框的宽、高，绘图框距屏幕左上角的左右、上下间距
turtle.width(5)
turtle.color('black')
turtle.penup()
turtle.goto(-100,-150)
#绝对坐标的原点在绘图框的中心位置
turtle.pendown()
for i in range(6):
    turtle.fd(200)
    turtle.left(180/3)
#方向转三次要与原方向反向
turtle.done()
