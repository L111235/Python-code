#z字形变换
'''将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串
 '''

#建一个有numRows个空字符串(或空列表）的列表，用字符串或列表的加法往里加字符：s=[''] * numRows  k=[[]]*numRows
#分两部分添加，竖的和斜的，斜的不包括头尾
#逆序可以用反向切片的形式完成：range(numRows-2,0,-1)，不包括0
s="PAYPALISHIRING"
numRows=3

if not numRows>1:
    print(s)
if numRows==2:
    s1=s[::2]
    s2=s[1::2]
    print(s1+s2)

s_Initialize = [''] * numRows
# print(s_row)
i = 0
n = len(s)
while i < n:
    for count_columns in range(numRows):
        if i < n:
            s_Initialize[count_columns] += s[i]  # 这里进行了将numRows个字符从上往下安置入每一行
            # print(s_row)
            i+=1
    # print(s_row)
    for count_Rows in range(numRows - 2, 0, -1):  # 这里进行了将numRows-2个字符从下往上安置入每一行
        if i < n:
        	s_Initialize[count_Rows] += s[i]
        	i+=1
print(''.join(s_Initialize))
