# A shop prints multiple copies of receipts. Use nested loops to print item numbers reapedly
"""
Created on Mon Mar 16 14:52:20 2026

@author: Diksha Nikam
"""
copies = 3
items_per_receipt = 4

# Outer loop: Handles the number of receipt copies
for copy_num in range(1, copies + 1):
    print(f"--- Receipt Copy #{copy_num} ---")
    
    # Inner loop: Prints each item number for the current copy
    for item_num in range(1, items_per_receipt + 1):
        print(f"Item {item_num}")
        
    print("------------------------\n")
