#Program for accepting two numerical integer values and find division
#Div3.py----Multi exceptions handling block
try:
	print("PVM Enters into try block")
	s1=input("\nEnter First Value:")
	s2=input("Enter Second Value:")
	a=int(s1) #----------------------erxception generated statement
	b=int(s2) #----------------------erxception generated statement
	c=a/b    #----------------------erxception generated statement
except  (ZeroDivisionError,ValueError):  # Multi exceptions handling block
	print("\nDON'T ENTER ZERO FOR DEN..")
	print("\nDON'T ENTER strs / symbols / alnums")
else:
	print("-----------------------------------")
	print("Val of a=",a)
	print("Val of b=",b)
	print("Div=",c)
	print("-----------------------------------")
finally:
	print("\nI am from finally Block")