#Program for accepting the data from KBD and write to the file.
#DynamicFileWriteOp1.py
with open("hyd.data","a") as fp:
	print("Enter the Data :")
	kbddata=input()
	fp.write(kbddata)
	print("Data written to the file")
