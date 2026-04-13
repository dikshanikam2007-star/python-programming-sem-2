# Create a Student class that calculates grade.
"""
Created on Mon Apr 13 15:12:44 2026

@author: DIKSHA
"""

class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def calculate_grade(self):
        avg = (self.m1 + self.m2 + self.m3) / 3
        
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"

s1 = Student("SUMIT", 85, 92, 78)
print(f"Student: {s1.name}")
print(f"Grade: {s1.calculate_grade()}")

