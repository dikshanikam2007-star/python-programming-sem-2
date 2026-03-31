# A ticket booking system repeats seat display pattern using loops.
"""
Created on Mon Mar 16 15:35:20 2026
@author: DIKSHA
"""

rows = 5
seats_per_row = 8

for r in range(1, rows + 1):
    print(f"Row {r}: ", end="") 
    
    for s in range(1, seats_per_row + 1):
        print(f"[{s}]", end=" ")
    print()  
