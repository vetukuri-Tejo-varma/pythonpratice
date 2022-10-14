#Program for accepting two numerical integer values and find division
#Div4.py
try:
	print("PVM Enters into try block")
	s1=input("\nEnter First Value:")
	s2=input("Enter Second Value:")
	a=int(s1) #----------------------erxception generated statement
	b=int(s2) #----------------------erxception generated statement
	c=a/b    #----------------------erxception generated statement
except  ZeroDivisionError as z:
	print(z)
except ValueError as hyd:
	print(hyd)
else:
	print("-----------------------------------")
	print("Val of a=",a)
	print("Val of b=",b)
	print("Div=",c)
	print("-----------------------------------")
finally:
	print("\nI am from finally Block")