#5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
		#Sample List : ['abc', 'xyz', 'aba', '1221']
		#Expected Result : 2


x=['121','131','abc','cda','ada']
s=[]
# c=0



for i in range(len(x)):
    if len(x[i])>2 and x[i][0]==x[i][-1]:
        s.append(x[i])
print(s)
print(len(s))       
        
        
# print(c)
# for i in x:

#     if len(x) > 2 and i[0]==i[-1]:
#         s.append(i)
# print(s)
# print(len(s))






