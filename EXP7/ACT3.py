# Create a Vehicle class to display fuel efficiency.
"""
Created on Mon Apr 13 15:21:36 2026

@author: DIKSHA
"""

class Vehicle:
    def __init__(self, model, distance, fuel_used):
        self.model = model
        self.distance = distance      
        self.fuel_used = fuel_used          
    def calculate_efficiency(self):
        if self.fuel_used <= 0:
            return 0
        return self.distance / self.fuel_used
    def display_efficiency(self):
        efficiency = self.calculate_efficiency()
        print(f"Vehicle Model: {self.model}")
        print(f"Distance:      {self.distance} km")
        print(f"Fuel Used:     {self.fuel_used} liters")
        print(f"Efficiency:    {efficiency:.2f} km/l")

car = Vehicle("Toyota Corolla", 500, 25)
car.display_efficiency()
