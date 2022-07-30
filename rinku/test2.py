# 3)CONVERTING CELSIUS TO FAREN

def convert_celsius_to_farenheat(h1):
    faren=(h1*(9/5))+32
    return faren
out=convert_celsius_to_farenheat(11)
print(out)

# 5)STORING IN SEPERATE LISTS
list=[4,5.5,"rinku","abc",7,22]
A=[]
B=[]
C=[]
for i in list:
    if type(i)==int:
        A.append(i)
    elif type(i)==float:
        B.append(i)
    elif type(i)==str:
        C.append(i)
print(A)
print(B)
print(C)


# 1)STRING IN ALPHABETICAL ORDER
word="it's  python class and you are a very brilliant student"
word.sort()
print(word)


9)PRIME NUMBERS
for n1 in range (50,101):
        for i in range(2,n1):
            if n1%i==0:
                break
        else:
            print(n1)




