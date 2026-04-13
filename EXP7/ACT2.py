# Create an Employee class that calculates salary with bonus.
"""
Created on Mon Apr 13 15:16:02 2026

@author: DIKSHA
"""

class Employee:
    def __init__(self, name, salary, bonus_percentage):
        self.name = name
        self.salary = salary
        self.bonus_percentage = bonus_percentage

    def calculate_total(self):
        bonus_amount = self.salary * (self.bonus_percentage / 100)
        return self.salary + bonus_amount

    def display(self):
        total = self.calculate_total()
        print(f"Employee: {self.name}")
        print(f"Total Salary (with {self.bonus_percentage}% bonus): {total}")

emp1 = Employee("Anagha", 50000, 20) 
emp1.display()
