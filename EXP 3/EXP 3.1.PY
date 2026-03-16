#1: Write a Python program using nested loops to print the following pattern for n rows
"""
Created on Mon Mar 16 15:08:34 2026

@author: DIKSHA
"""
n = int(input("Enter number of rows:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
      print(j, end=" ")
    print()
