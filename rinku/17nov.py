

class room:
    def __init__(self, l, b):
        self.length = l
        self.breadt = b
        self.area = l * b

    def __add__(self, other):
        a = self.area + other.area
        print("total area", a)

    def __sub__(self, other):
        a = self.area - other.area
        print("area difference", a)

    def __lt__(self, other):
        if self.area < other.area:
            print(True)
        else:
            print(False)

    def __gt__(self, other):
        if self.area > other.area:
            print(True)
        else:
            print(False)


r1 = room_area(10, 5)
r2 = room_area(20, 10)
r1 + r2
r1 - r2
r1 > r2
r1 < r2
