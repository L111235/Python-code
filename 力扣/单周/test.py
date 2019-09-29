'''5206.删除字符串中的所有相邻重复项'''
s = "deeedbbcccbdaa"
k = 3
i=0
n=len(s)
while(i+k<=n):
	if s[i:i+k]==s[i]*k:
		#1.采用切片结合字符串的乘法来进行对比处理
		#2.或者将字符逐个对比，累计相同字符的个数然后与k对比
		#3.或者将字符逐个添加到一个list中，进行set处理，看
		#处理之后长度是否为1
		#后面两种方法花费时间比第一种方法更长
		s=s[:i]+s[i+k:]
		n=n-k
		if i-k>0:
			i-=k
		else:
			i=0
	else:
		i+=1
print(s)