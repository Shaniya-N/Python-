class Car():
    def __init__(self,model,color="Black"):
        self.model = model
        self.color=color
        print(color)
    def milage(self):
        print(f"{self.model.title()} has good milage")
    def speed(self):
        print(f"{self.model.title()} has good speed")

my_car=Car("WagonR","White")
print(f"I own a {my_car.model.capitalize()}")
my_car.milage()