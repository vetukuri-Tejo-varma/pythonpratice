from MulTableExcept import NegNumError,ZeroError
def table(n):
    if(n<0):
        raise NegNumerror
    if(n==0):
        raise ZeroError
    if n>0:
        print("\nmulable for {}".format(n))
    for i in range(1,11):
        print("\t{}x{}={}".format(n,i,n*i))