#3. Write a Python program to get the largest number from a list. 
x=[3,4,6,5,2]

large=x[0]
for i in range(len(x)):
    if x[i] >large:
        large=x[i]
print(large)



