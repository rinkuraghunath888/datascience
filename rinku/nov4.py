# class student:
#     college='techolas'
#     def __init__(self,name,id):
#         self.id=id
#         self.name=name
#     def details(self):
#         print(self.id,self.name,student.college)
#
# s1=student('rinku',52,)
# s1.details()

# class employee:
#     company='techolas'
#     def __init__(self,name,id,salary):
#         self.id=id
#         self.name=name
#         self.salary=salary
#     def details(self):
#         print(self.id,self.name,self.salary,employee.company)
#
# c1=employee('rinku',52,25000)
# c1.details()

class ticket:
    count=0
    def __init__(self,train_name):
        self.tname=train_name
    def book_ticket(self):
        print("BOOKED")
        ticket.count=ticket.count+1
    def count_ticket(self):
        print("booked ticket:",ticket.count)
parasu=ticket("parasu")
parasu.book_ticket()
parasu.book_ticket()
parasu.book_ticket()
parasu.count_ticket()