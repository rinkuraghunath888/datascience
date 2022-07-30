# num_list=[1,4,2,6,200]
# def find_max(num_list:list):
#     num_list.sort(reverse=True)
#     print(num_list[0])
#
# find_max(num_list)

# def is_right_traiangle(a,b,c):
#     sides=[a,b,c]
#     sides.sort(reverse=True)
#     if sides[0]**2==sides[1]**2+sides[2]**2:
#         print("its a right triangle")
#     else:
#         print("its not a rigt triangle")
#
# is_right_traiangle(3,4,6)

# num_list=[1,4,2,6,2]
# def sum_of_list(numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print(sum)
#
# sum_of_list(num_list)

# def find_sum(num1,num2=0,num3=0,num4=0,num5=0):
#     print(num1+num2+num3+num4+num5)
# find_sum(1,2,3,4,5,)

def find_area(num1,num2=0):
    if num2!=0:
        area1=num1+num2
        print(f"area of rectangle is {area1}")
    else:
        area2=3.14*num1*num1
        print(f"area of circle is {area2}")
find_area(4)






