class Students:
    def __init__(self,name,adress,marks):
        self.name=name
        self.adress=adress
        self.mark=mark
    def print_details(self):
        print(self.name,self.adress,self.mark)
class College(Students):
    def __init__(self,Cname,loc):
        self.Cname=Cname
        self.loc=loc
    def admit(self,stud:Students):
        if self.mark >= 80:
            print(f"{self.name} is admitted to {self.Cname}")
        else:
            print(f"{self.name}is not qualified")
stud=Students("rinku","st.joseph",45)
col=College("st.joseph's ","Banglore")
stud.print_details()
