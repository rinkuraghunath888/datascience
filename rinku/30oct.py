class laptop:
    name=''
    company=''
    ram=''
    def shutting_down(self):
        print("machine is shutting down")
    def play_vedios(self):
        print("playing vedios...")


obj=laptop()
obj.name='ASUS VIVO BOOK'
obj.company='ASUS'
obj.ram='16gb'
obj1=laptop
obj1.name='hp pav'
obj1.company='HP'
obj1.ram='8gb'

print(obj.name,obj.company,obj.ram)
obj1.shutting_down()

