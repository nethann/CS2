class Location: 
    def __init__(self,x,y): 
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'


class Car: 
    def __init__(self, car_name:str, location:Location, cost_per_mile:float): 
        self.car_name = car_name
        self.location = location 
        self.cost_per_mile = cost_per_mile

    def __str__(self): 
        return f'[{self.car_name}, {self.location}, {self.cost_per_mile}]'

    def move_to(self, new_x, new_y): 
        return Location.self.x



Loc = Location(1,2)
Cr = Car('toyota', Loc, 20)
print(Cr)

