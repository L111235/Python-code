a=input()
b=pow(eval(a),3)
print('{:-^20}'.format(b))

'''以上代码可改写为：
a=eval(input())
print('{:-^20}'.format(pow(a,3)))'''
