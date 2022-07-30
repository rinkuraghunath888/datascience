a1 = int(input("enter a nmbr"))
days={1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday',7:'sunday'}
print(days.get(a1,"invalid"))

name = input("enter your name :")
print(name)
age = int(input("enter your age"))
print(age)
loc = input("enter ur location :")
print(f"hai am {name} my age is {age}coming from {loc} ")

EVEN NUMBER
for i in range(2,100,2):
    print(i)

SUM OF EVEN ODD
sumE=0
sumO=0
for i in range(1,101):
    if i % 2 == 0:
        sumE=sumE+i
    else:
        sumO=sumO+i
print(f"sum of even number is {sumE}")
print(f"sum of odd numbers is {sumO}")

