import pickle
with open("rmp.data","ab") as fp:
    while(True):
        try:
            eno=int(input("Enter Employeee  number"))
            ename=input("Enter Employee name")
            sal=float(input("enter employee salary"))
            lst=list()
            lst.append(eno)
            lst.append(ename)
            lst.append(sal)

            pickle.dump(lst,fp)
            ch=input("do u want to insert another record(yes/no")
            pickle.dump(lst,fp)
            if(ch.lower()=="no"):
                print("thanks")
                break
        except ValueError:
            print("dont enter symbols")