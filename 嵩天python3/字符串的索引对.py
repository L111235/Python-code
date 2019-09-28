text = "thestoryofleetcodeandme"
words = ["story","fleet","leetcode"]
tmp=[]
for i in range(len(text)):
    for j in range(i,len(text)+1):
        if text[i:j] in words:
            tmp.append([i,j-1]) 
print(tmp)
