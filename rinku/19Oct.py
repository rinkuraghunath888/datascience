# print("koooi")
# def sample():
#     print("hello")
#     print("welcome")
# print("hiiiiii")
# sample()
# print("where r u")

# def print_company_name():
#     print("techolas")
#
# print("hai")
# print_company_name()
# print("bye")
# print_company_name()

# def find_square(num):
#     print("hai")
#     print(num*num)
# find_square(4)
#
# def get_pi():
#     print("this function is to get the value of pi")
#     return 3.14
# radius=10
# area=get_pi()*radius*radius
# pm=2*get_pi()*radius
# print(area,pm)

def is_right_traiangle(a,b,c):
    sides=[a,b,c]
    sides.sort(reverse=True)
    if sides[0]**2==sides[1]**2+sides[2]**2:
        print("its a right triangle")
    else:
        print("its not a rigt triangle")

is_right_traiangle(3,4,6)