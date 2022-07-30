# # EXAMPLE 1
# class Vechicle:
#     def __init__(self,colour,engine_size,fuel_type):
#         self.colour=colour
#         self.engine_size=engine_size
#         self.fuel_type=fuel_type
#     def start_engine(self):
#         print("engine started")
#     def apply_break(self):
#         print("break applied")
#
# class Car(Vechicle):
#     def __init__(self,color,es,ft,tra):
#         super().__init__(color,es,ft)
#         self.transmission=tra
#     def open_sun_roof(self):
#         print("car sun roof opened")
# c1=Car("black",1800,"petrol","amt")
# c1.open_sun_roof()
# c1.start_engine()
# c1.apply_break()


class Human:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.adress=address
    def print_details(self):
        print(self.name,self.age,self.adress)
class Employee(Human):
    def __init__(self,name,age,add,desig,company,salary):
        super().__init__(name,age,add)#INHERITANCE
        self.desig=desig
        self.comapny=company
        self.salary=salary
    def print_professional_details(self):
        print(self.desig,self.comapny,self.salary)
e=Employee("rinku",30,"wayanad","tcs","engineer",30000)
e.print_details()
e.print_professional_details()


