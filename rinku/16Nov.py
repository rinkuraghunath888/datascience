class sample:
    def __init__(self,a):
        self.a=a
    def execute(self):
        print("hai \n this is class sample")
class new(sample):
    def executes(self):#CONSTRUCTOR OVERRIDING('execute' of new class over ride the function)
        print("helooo \n this is new class")

obj=new(10)
obj.execute()
