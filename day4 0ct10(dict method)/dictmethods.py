d={}
#pin=int(input("enter pincode"))
d.update(name=input("enter name"),email=input("enter email"),mobileno=int(input("enter mobile no")),city=input("enter state"),pincode=int(input("enterpin")))
for i,j in d.items():
     print(i,"=",j,end="")
d.update(name=input("enter name"))
print(d)
keys=input("enter the key")
rem=d.pop(keys)
print(rem)
print(d)
value=input("enter a value")
if value in d.items():
     print('value exist')
else:
     print('value does not exists')
d.update(state=input("enter state"))
print(d)


