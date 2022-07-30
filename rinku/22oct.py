# def find_total(name,mark1,mark2,mark3,mark4,mark5):
#     total=mark1+mark2+mark3+mark5+(mark4*120/100)
#     print(f"hai{name} your total is{total}")
#
# find_total("rinku",mark1=25,mark3=50,mark4=32,mark2=44,mark5=50)

# def find_sum(*a):
#     sum=0
#     for i in a:
#         sum=sum+i
#     print(sum)
#
# find_sum(3,45,55,66,77,33)

def print_student_details(name,*m):
    # input("enter the name")
    # int(input("mark"))
    for i in m:
        sum=sum+i
        print(f"{name}mark is {sum}")
print_student_details("rinku",23, 35,50,50)
