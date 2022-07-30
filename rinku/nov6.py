class Train:
    def __init__(self,number,name,sstation,estation,stations:list):
        self.train_number=number
        self.tname=name
        self.start_station=sstation
        self.end_station=estation
        self.current_station=sstation
        self.stations=stations
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


stations = ["kasargod", "kannur", 'calicut', 'trissur', 'ernakulam']
parassu=Train(13420,'parassuram express','kasargod','eranakulam',stations)

parassu.print_train_details()
parassu.start_engine()
parassu.stop_engine()


