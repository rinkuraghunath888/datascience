class Patient:
    def __init__(self, name, age, loc):
        self.name = name
        self.age = age
        self.loc = loc
        self.medicine=''
        self.desease=''
    def get_my_medicines(self):
        print("---------------------------------------")
        print(self.name,self.age)
        print("desese:",self.desease)
        print("medicine:",self.medicine)
        print("========================================")

class Doctor:
    def __init__(self,name,dept,fee):
        self.name=name
        self.dept=dept
        self.fee=fee
    def consult(self,pat:Patient):
        print(f"Dr.{self.name} consulting patient {pat.name}")
        pat.desease="fever"
        pat.medicine="parasetamole"
doct=Doctor("Ajay","ortho",250.0)
pa=Patient("Biju",34,"calicut")
doct.consult(pa)
pa.get_my_medicines()
