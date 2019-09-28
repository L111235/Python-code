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
        
listi=['']*numRows
i=1
listi[0]+=s[0]
count=0
while i <len(s):
    for k in range(1,numRows):
    	if i<len(s):
    #每进行字符串相加之前，都要进行这个判定，以免超过字符串s的长度，并且该判定要在相加之前，不然
    #很难对s[len(s)-1]这个字符进行处理
        	listi[k]+=s[i]
        	i+=1
        	#i+=1减去一个缩进，不过下面的判断语句需要进行变动
                
    if i==len(s):
        break
    listi.reverse()
    count+=1#记录翻转次数
            
sre=''
if count%2==0:
	#sre=''.join(listi)
    for k in range(numRows):
        sre+=listi[k]
    print(sre)
if count%2==1:
    listi.reverse()
    #sre=''.join(listi)
    for k in range(numRows):
        sre+=listi[k]
    print(sre)