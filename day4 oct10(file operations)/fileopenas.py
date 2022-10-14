with open("stud.data","r") as fp:
    print("type",type(fp))
    print(fp.name)
    print("mode",fp.mode)
    print("file read",fp.readable())
    print("file write",fp.writable())
    print("file closed",fp.closed)
print("close", fp.closed)