import turtle as t
t.setup(700,400,200,200)
t.width(25)
t.color('purple')
#color函数的参数为字符串
t.penup()
t.bk(300)
t.pendown()
t.seth(-45)
'''设定海龟当前朝向角度（绝对坐标，与之前海龟朝向角度无关）。right和left函数改变
海龟朝向角度与之前海龟朝向角度有关'''
for i in range(4):
#range是循环函数，round取四舍六入（如果是5则取相邻的偶数）函数
    t.circle(40,90)
    t.circle(-40,90)
#circle中的角度得是之前seth中设置角度的两倍，不然图形不能保持水平
t.circle(40,45)
t.seth(0)
t.fd(40)
t.circle(25,180)
t.fd(15)
t.done()
