#Program for demonstarting reading the data from file--readlines()
#FileReadEx2.py
try:
	filename=input("Enter File Name:")
	with open(filename,"r") as fp:
		filedata=fp.readlines()
		print("-"*50)
		for line in filedata:
			print(line,end="")
		print("-"*50)
except FileNotFoundError:
	print("File does not exist")