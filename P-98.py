def swapFileData():
    f1= input("enter file1 name:-")
    f2= input("enter file2 name:-")

    with open(f1,'r') as a:
        data_a= a.read()

    with open(f2,'r') as b:
        data_b= b.read()

    with open(f1,'w') as a:
       a.write(data_b)

    with open(f2,'w') as b:
        b.write(data_a)
swapFileData()