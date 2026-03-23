# Find the factorial of a number using loops.
"""
Created on Mon Mar 23 15:57:16 2026

@author: DIKSHA
"""

n = int(input("Enter number:"))
fact = 1
for i in range(1, n + 1):
 fact = fact * i
print("Factorial:", fact)
