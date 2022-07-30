class student:
    school_name="TECHOLAS"
    def __init__(self,roll,name,marks1,marks2,marks3):
        self.id=roll
        self.name=name
        self.mark1=marks1
        self.mark2=marks2
        self.mark3=marks3
    def print_details(self):
        print(f"{self.id}\n{self.name}\n{self.mark1+self.mark2+self.mark3}")

    @classmethod
    def get_school_name(cls):
        print(cls.school_name)
        student.get_school_name()

rinku=student(11,'rinku',42,23,45)
rinku.print_details()

    @staticmethod
            def find_pass_or_not()
                if mark>50:
                    print("passed")
                else:
                    print("failed")

student.find_pass_or_not()



