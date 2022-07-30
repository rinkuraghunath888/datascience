f=1
num= int(input("enter a number"))
if num < 0:
   print("factorial does not exist ")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       f = f*i
   print(f"The factorial of{num} is {f}")


# for i in range(3,11):
#     sqr= i ** 2
#     print(sqr)
# n1=int(input("enter a num"))
# for i in range(1,n1+1):
#     cube=i*i*i
# print(f"current nbr is{n1}and cube is{cube}")
