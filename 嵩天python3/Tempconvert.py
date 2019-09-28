#Tempconvert.py
Tempstr=input("请输入带有符号的温度值（符号后置 华氏为F摄氏为C）：")
#Tempstr：温度字符串。string
if Tempstr[-1] in ['F','f']:
    #如果[]中只有一个字符串，in可以用==代替，同时必须去掉[]
    #假如Tempstr的倒数第一个字符是字符F或f中的其中一个
    C=(eval(Tempstr[0:-1])-32)/1.8   
    #eval（）去掉参数最外侧引号并执行余下语句的函数
    #[0:-1]中0代表Tempstr字符串中的第一个字符，0：-1表示第一个到倒数第二个字符
    #[0:]表示第一个到最后一个字符
    print("转换后的温度是{:.2f}C".format(C))
    #{}表示槽，后续变量填充到槽中,{:.2f}表示将变量C填充到这个位置时取小数点后2位
elif Tempstr[-1] in ['C','c']:
    F=1.8*eval(Tempstr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")


#[0:3]相当于[:3]
