l1=[]
print("*"*50)
n=int(input("how many elemant"))
print("*"*5,type(l1))
print("\t1.for add value:")
print("\t2.for pop")
print("\t3.exit")
print("*"*50)
ch=int(input("you are ops:"))
if(ch==1):
    print("-"*50)
    print("\tadd values")
    for i in range(0,n):
        l1.append(input("give value:"))
    print(l1)
    print("-"*5,">")
    p=int(input("you pop the  num:"))
    if (p==0):
        print(l1)
        c=int(input("pop index num"))
        l1.pop(c)
        print(l1)
elif(ch==2):
    print("\tpop index value:")
    k=int(input("how many you pop"))
    if(k>1):
        print("okay kan")
        for j in range(k):
            print("1 is not taken")
else:
    print("thank you")
    exit()
