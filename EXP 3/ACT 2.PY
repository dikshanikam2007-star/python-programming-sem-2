#A school generates multiplication tables for students from 1 to 10.
"""
Created on Mon Mar 16 15:30:09 2026
@author:DIKSHA
"""

for i in range(1, 11):
    print(f"Multiplication Table for {i}:")
    
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
    
    print("-" * 15) 
