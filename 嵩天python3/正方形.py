import turtle
turtle.setup(500,400,300,200)
#绘图框的宽、高，绘图框距屏幕左上角的左右、上下间距
turtle.width(5)
turtle.color('black')
turtle.penup()
turtle.goto(-100,-100)
#绝对坐标的原点在绘图框的中心位置
turtle.pendown()
for i in range(4):
    turtle.fd(200)
    turtle.left(90)
turtle.done()

