#write a python program which will find number of lines, no of words, no of characters in a given file
#FileCounfInfo.py
filename=input("Enter any file name:")
try:
	with open(filename) as fp:
		filelines=fp.readlines()
		nl,nw,nc=0,0,0
		for line in filelines:
			nl=nl+1
			nw=nw+len(line.split())
			nc=nc+len(line)
		else:
			print("-"*50)
			print("Number of Lines=",nl)
			print("Number of Words=",nw)
			print("Number of Chars=",nc)
			print("-"*50)

		
except FileNotFoundError:
	print("File does not exist")