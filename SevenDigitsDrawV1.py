#SevenDigitsDrawV1.py
import turtle as p
def drawline(draw):    #绘制单段数码管
    p.pendown() if draw else p.penup()
    p.fd(40)
    p.right(90)
def drawDigit(digit):  #根据数字绘制七段数码管并将海龟右移20个像素
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    p.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    p.left(180)
    p.penup()
    p.fd(20)
def drawData(data):  #获得要输出的数字
    for i in data:
        drawDigit(eval(i))   #通过eval()函数将数字字符串变成整数
def main():
    p.setup(800,350,200,200)
    #p.hideturtle()   #绘制开始前隐藏海龟
    p.penup()
    p.fd(-300)
    p.pensize(5)
    drawData('20190505')
    p.hideturtle()   #在绘制完成后隐藏海龟
    p.done()
main()
