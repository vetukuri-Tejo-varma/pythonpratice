import pickle
try:
    with open("rmp.data","rb") as fp:
        print("empno\tname\tsalary")
        while(True):
            try:
                obj=pickle.load(fp)
                for val in obj:
                    print("{}".format(val),end="\t")
                print()
            except EOFError:
                    break
except FileNotFoundError:
    print("file does not exist")