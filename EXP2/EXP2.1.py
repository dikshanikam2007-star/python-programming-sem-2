# Check whether a given year is a leap year.
"""
Created on Mon Mar 23 15:51:32 2026

@author: DIKSHA
"""

year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
  print("Leap Year")
else:
  print("Not a Leap Year")
