class Person:
    def __init__(self,name,loc,phn):
        self.name=name
        self.loc=loc
        self.phn=phn
    def print_details(self):
        print(self.name,self.phn,self.loc)

class Shop:
    def __init__(self,shopname,ownername):
        self.shop_name=shopname
        self.owner_name=ownername
        self.customers=[]
    def register_customer(self,per:Person):
        self.customers.append(per)
    def customer_details(self):
        for p in self.customers:
            p.print_details()

shop=Shop('vivek','raghu')
rahul=Person('rahul','calicut','4567890876')
reena=Person("reena","kannur","546789098")
rinku=Person("rinku","malappuram","56786789")
shop.register_customer(rahul)
shop.register_customer(reena)
shop.register_customer(rinku)
shop.customer_details()



# class Person:
#     def __init__(self,name,loc,phn):
#         self.name=name
#         self.loc=loc
#         self.phn=phn
#     def print_details(self):
#         print(self.name,self.loc,self.phn)
#
# class Shop:
#     def __init__(self,shpname,ownername,):
#         self.shop_name=shpname
#         self.owner_name=ownername
#         self.customers=[]
#     def register_customer(self,per:Person):
#         self.customers.append(per)
#     def customer_details(self):
#         for p in self.customers:
#             p.print_details()
# shp=Shop('vivek','raghunathan')
# rahul=Person('rahul','kalpetta','9662')
# shp.register_customer(rahul)
# shp.customer_details()