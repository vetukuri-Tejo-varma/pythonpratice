#Program for demonstarting Writing the data to the file--write()
#FileWriteEx1.py
with open("addr1.data","a") as fp:
	fp.write("James Gosling\n")
	fp.write("13-94, Hill stattion\n")
	fp.write("Sun Micro System\n")
	fp.write("USA-12\n")
	print("Data Written to the file")