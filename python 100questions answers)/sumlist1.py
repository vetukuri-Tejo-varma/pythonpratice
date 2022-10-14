#Write a Python program to sum all the items in a list.
# x=[1,2,3,4,5]
# sum=0
# for i in range(len(x)):
#     sum=sum+x[i]
# print(sum)
#list comphreshsion:
x = [1, 2, 3, 4, 5]
sum=0
[sum:=sum+val for val in x]
print(sum)