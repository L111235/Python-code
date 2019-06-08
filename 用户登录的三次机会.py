for i in range(3):
    user=input()
    password=input()
    if user=='Kate' and password=='666666':
        print('登录成功！')
        break
if user!='Kate' or password!='666666':
    print('3次用户名或者密码均有误！退出程序。')

'''
if i==2:
    print('3次用户名或者密码均有误！退出程序。')

可能最后一次输入正确

'''




'''
count = 0
while count < 3:
    name = input()
    password = input()
    if name == 'Kate'and password == '666666':
        print("登录成功！")
        break
    else:
        count += 1
        if count == 3:
            print("3次用户名或者密码均有误！退出程序。")
'''
