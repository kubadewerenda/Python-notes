class Car:
    def __init__(self, model, year, color, for_sale):#__ dunder
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive a {self.color} {self.model}")
    
    def stop(self):
        print(f"You stop a {self.color} {self.model}")

    def dsecribe(self):
        print(self.model, self.year, self.color)