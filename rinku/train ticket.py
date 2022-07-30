class Ticket:
    num=153767
    def __init__(self,name,age,fromloc,to,fare):
        self.name=name
        self.age=age
        self.fromloc=fromloc
        self.toloc=to
        self.fare=fare
        Ticket.num=Ticket.num+1
        self.ticketnumber="IRCTC"+str(Ticket.num)
    def display_ticket(self):
        print("-------------------------")
        print(f"{self.ticketnumber}\n{self.name}-{self.age}\n{self.fromloc} to {self.toloc}\n"
              f"{self.fare}\n========================================")
class Train:
    def __init__(self,number,name,stations:list):
        self.train_number=number
        self.tname=name
        self.start_station=stations[0]
        self.end_station=stations[-1]
        self.current_station=stations[0]
        self.stations=stations
        self.is_moving=False
        self.tickets=[]
    def book_tickets(self,tic:Ticket):
        self.tickets.append(tic)
    def display_all_tickets(self):
        for i in self.tickets:
            i.display_ticket()




    def move_train(self):
        if self.is_moving==False and self.current_station!=self.end_station:
            print("train starts moving...")
            self.is_moving=True
        else:
            print("sorry the train is moving now or its in the destination..")
    def stop_train(self):
        if self.is_moving==True:
            indx=self.stations.index(self.current_station)
            self.current_station=stations[indx+1]
            print("train stops at",self.current_station)
            self.is_moving=False
        else:
            print("train already stopped")


    def start_engine(self):
        if self.start_station==self.current_station:
            print("starting engine")
        else:
            print("not able to start engine because train is "
                  "currently not at the start station")
    def stop_engine(self):
        if self.end_station==self.current_station:
            print("stopping engine")
        else:
            print("not able to stop engine because train is "
                  "currently not at the end station")
    def print_train_details(self):
        print("------------------------------------------------------")
        print(f"{self.train_number}:{self.tname}\n{self.start_station} to {self.end_station}")
        if self.is_moving==True:
            indx=self.stations.index(self.current_station)
            print(f"train departs from {self.current_station}\n"
                  f"next station is {self.stations[indx+1]}")
        else:
            print(f"train halts at {self.current_station}")
        print("---------------------------------------------------------")

stations=["kasargod","kannur",'calicut','trissur','ernakulam']
parassu=Train(13420,'parassuram express',stations)
#
# parassu.print_train_details()
# parassu.start_engine()
# parassu.move_train()
# parassu.print_train_details()
#
t1=Ticket("mithun",27,"kannur","trissur",220)
t2=Ticket("suhail",25,"kasargod","calicut",130)
parassu.book_tickets(t1)
parassu.book_tickets(t2)

parassu.display_all_tickets()