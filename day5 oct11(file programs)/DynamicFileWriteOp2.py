#Program for accepting the data from KBD and write to the file.
#DynamicFileWriteOp2.py
import sys
with open("hyd.data","a") as fp:
	print("Enter the Data and press (stop) to terminate:")
	while(True):
		kdata=input()
		if(kdata=='stop'):
			print("\nComplete data written to the file")
			sys.exit()
		else:
			fp.write(kdata+"\n")
		
