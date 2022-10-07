from MulTableExcept import NegNumError,ZeroError
from MulTable import table
try:
    n=int(input("enter a table"))
    table(n)
except ZeroError:
    print("\n dont enter zero for mul table")
except NegNumError:
    print("\n dont enter strs/special symbols/alnum")
except:
    print("something went wrong")