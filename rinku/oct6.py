names=[]
mark1=[]
mark2=[]
for i in range(3):
    n1=input("enter names")
    m1=int(input("enter first mark"))
    m2=int(input("enter second mark"))
    names.append(n1)
    mark1.append(m1)
    mark2.append(m2)
    print(names)
    print(mark1)
    print(mark2)
for i in range(len(names)):
    print(names[i],mark1[i]+mark2[i])