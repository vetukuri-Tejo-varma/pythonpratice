#Program for demonstarting Writing the data to the file--writelines()
#FileWriteEx2.py
x={10:"Python",20:"Java",30:"R"}
with open("add2.data","a") as fp:
	fp.writelines( str(x)+"\n" )
	print("Iterable object Data written to the file")