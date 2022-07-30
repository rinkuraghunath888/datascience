# class students:
#     def __init__(self,name,rollnmbr,age):
#         self.name=name
#         self.rollnumr=rollnmbr
#         self.age=age
#     def start_learning(self):
#         print("start_learning")
#     def go_to_school(self):
#         print("go_to _school")
#
# s1=students("rinku",55,25)
# s2=students("rahul",62,22)
# print(s1.name,s1.rollnumr,s1.age)
# print(s2.name,s2.rollnumr,s2.age)

# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#
#     def find_area(self):
#         area=3.14*self.radius**2
#         print(f"area of circle is {area}")
#     def find_perimeter(self):
#         perimeter=2*3.14*self.radius
#         print(f"perimeter is {perimeter}")
# c1=circle(10)
# c2=circle(20)
# c1.find_area()
# c1.find_perimeter()

# class rectangle:
#     def __init__(self,length,bredth):
#         self.length=length
#         self.bredth=bredth
#     def find_area(self):
#         area=self.length*self.bredth
#         print(f"area of rectangle is {area}")
#     def find_perimeter(self):
#         perimeter=2*(self.length+self.bredth)
#         print(f"perimeter is {perimeter}")
# r1=rectangle(5,4)
# r2=rectangle(5,6)
# r1.find_area()
# r1.find_perimeter()

class measurement:
    def __init__(self,length):
        self.l=length
    def get_length_in_cm(self):
        lm=100*self.l
        print(f"length in meter is {lm}")
    def get_length_in_km(self):
        lk=self.l/1000
        print(f"length in kilometer is{lk}")
l1=measurement(10)
l1.get_length_in_cm()
l1.get_length_in_km()

