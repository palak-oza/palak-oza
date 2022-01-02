while True:
    a=int(input("Enter number of names in list 1: "))
    b=int(input("Enter number of names in list 2: "))
    l1=[]
    l2=[]
    sum=0
    temp=[]
    print("FOR LIST 1")
    for i in range(a):
        c=input("Enter name of the hotel: ")
        l1.append(c)

    print("FOR LIST 2")
    for j in range(b):
        d=input("Enter name of the hotel: ")
        l2.append(d)

    for k in range(a):
        for l in range(b):
            if(l1[k]==l2[l]):
                sum=k+l
                temp.append(sum)
                s=min(temp)
                if(s is min(temp)):
                    print("Hotel of matching list is: ")
                    print(l1[k])
    ch=input("Do you want to continue(y/n): ")
    if(ch=='n' or ch=='N'):
        break


