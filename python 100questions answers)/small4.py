#4. Write a Python program to get the smallest number from a list.

x=[3,5,2,6,7]
small=x[0]
for i in range(len(x)):
    if x[i] < small:
        small=x[i]
print(small)

