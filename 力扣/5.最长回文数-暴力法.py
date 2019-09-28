#5.最长回文数-暴力法.py
s="babad"
if len(s)==0:
    print('')
max_len=1
max_str=s[0]
i=0
while i<len(s):
    j=i+1
    while j<len(s):
        #建一个临时字符串，解决切片字符串不方便反转的问题
        temp=s[i:j+1]
        if s[j]==s[i] and temp==temp[::-1]:
            if len(temp)>max_len:
                max_len=len(temp)
                max_str=temp
        j+=1
    i+=1
print(max_str) 