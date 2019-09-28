#coding=utf-8
import os
#获取目标文件夹的路径
filedir=r"E:\1"

new_file=u"%s\**.ts" % filedir #合并之后的视频，视频名字为**.ts
f=open(new_file,'wb+') #二进制文件写操作

for i in range(0,1166): #从数字遍历，用于拼接视频片段名字
    filepath=u"%s\%d.ts" % (filedir,i) #视频片段名字
    print(filepath)
    #遍历单个文件，读取行数
    for line in open(filepath,'rb'): #循环读取每一个视频片段
        f.write(line)  #将视频片段写入合并后的文件
    f.flush  #刷新输出流

#关闭文件
f.close()
