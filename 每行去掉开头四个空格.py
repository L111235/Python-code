def jiantabe(infile,outfile):
	f=open(infile,'r',encoding='utf-8')
	fw=open(outfile,'w',encoding='utf-8')
	for line in f.readlines():
		line=line.rstrip('\n')#去掉末尾的回车，因为每写入一行会自动加一个回车
		if len(line)>4:#每行长度不能小于5
			if line[0] is ' ':#判断每行开头是不是tabe，是就去掉
				line=line[4:]
		print(line)
		print(line,file=fw)#要写fw，不能写outfile
	f.close()
	fw.close()

jiantabe('1.py','out.py')