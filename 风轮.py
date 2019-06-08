import turtle as t
t.setup(600,600,300,200)
#绘图框的宽、高，绘图框距屏幕左上角的左右、上下间距
t.width(2)
t.color('black')
t.left(45)
for i in range(2):
    t.fd(150)
    t.left(90)
    #圆弧与当前朝向相切
    t.circle(150,360/8)
    t.left(90)
    t.fd(150)
    t.right(45)
t.seth(135)
for j in range(2):
    t.fd(150)
    t.left(90)
    t.circle(150,360/8)
    t.left(90)
    t.fd(150)
    t.right(45)
t.done()
