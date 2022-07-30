class Train:
    def __init__(self,number,name,stations:list):
        self.train_number=number
        self.tname=name
        self.start_station=stations[0]
        self.end_station=stations[-1]
        self.current_station=stations[0]
        self.stations=stations
        self.is_moving=False

    def move_train(self):
        if self.is_moving==False and self.current_station!=self.end_station:
            print("train starts moving...")
            self.is_moving=True
        else:
            print("sorry the train is moving now or its in the destination..")
    def stop_train(self):
        if self.is_moving==True:
            index=self.stations.index(self.current_station)
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

parassu.print_train_details()
parassu.start_engine()
parassu.move_train()
parassu.print_train_details()