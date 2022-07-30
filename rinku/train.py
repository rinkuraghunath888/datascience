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
        if self.is_moving==False and self.current_station!=self.endstation:
            print("train is moving...")
            self.is_moving=True
        else:
            print("sorry the train is movingor its in the destination")
    def stop_train(self):
        if self.is_moving==True:
            indx=self.stations.index(self.current_station)
            self.current_station=stations[indx+1]
            print("train stops at"self.current_station)
        else:
            print("train is already stopped")


    def start_engine(self):
        if self.start_station==self.current_station:
            print("start engine")
        else:
            print("not able to start bcoz train not at start station")
    def stop_engine(self):
        if self.end_station == self.current_station:
            print("stop engine")
        else:
            print("not able to stop bcoz train not at end station")
    def print_train_details(self):
            print(f"{self.train_number}:{self.tname}\n{self.start_station} to {self.end_station}\n"
                  f"current station:{self.current_station}")

        print(f"train departs from {self.current_station} next station is {self.end_station}")
    def stop_train(self):
        if self.is moving==True:
            print("")

stations = ["kasargod", "kannur", 'calicut', 'trissur', 'ernakulam']
parassu=Train(13420,'parassuram express',stations)

parassu.print_train_details()
parassu.start_engine()
# parassu.stop_engine()
parassu.move_train()