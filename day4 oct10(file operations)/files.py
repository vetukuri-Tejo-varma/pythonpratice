try:
    f=open("stud.data")
except FileNotFounderror:
    print("\n file does not  error")
else:
    print("Type of fp",type(f))
    print(f.name)
    print(f.readable)
    print(f.writable())
    print(f.closed())
finally:
    f.close()
    print("closed",f.closed)