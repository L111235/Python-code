a=1
#给定初始能力值以便while函数能正确运行
dayupdef=0.009
while a<pow(1.01,365):
    a=1
    #每次for循环结束后要将初始能力值重置
    dayupdef+=0.001
    #要放在for循环语句之前
    for i in range(365):
        if i%7 in [0,6]:
            a=a*0.99
        else:
            a=a*(1+dayupdef)

#print(a)
print('工作日的努力参数是:{:.3f}'.format(dayupdef))
#给定精度为3以去掉浮点数尾数
