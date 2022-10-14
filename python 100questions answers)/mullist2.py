#2. Write a Python program to multiply all the items in a list.
y=[1,2,3,4,5]
# mul=1
# for i in range(len(y)):
#     mul=mul*y[i]
# print(mul)

mul=1#list comphresion
[mul:=mul*val for val in y]
print(mul)