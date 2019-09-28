def getText():
    txt = open("hamlet.txt", "r").read()
    print(type(txt))
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt

hamletTxt = getText()
words  = hamletTxt.split()
counts={}
for word in words:
    if word not in counts:
        counts[word]=1
    else:
        counts[word]+=1
#print(counts)
items = counts.items()
print(items)
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(10):
    word, count = items[i]
    # print ("{0:<10}{1:>5}".format(word, count))  输出出现最多的10个单词和其出现次数
    print (word)  #输出出现最多的10个单词