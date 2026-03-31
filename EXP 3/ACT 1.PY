# A shop prints multiple copies of receipts. Use nested loops to print item numbers reapedly
"""
Created on Mon Mar 16 14:52:20 2026

@author: DIKSHA
"""
num_receipts = 3
items_per_receipt = 4

for receipt_num in range(1, num_receipts + 1):
    print(f"--- Receipt #{receipt_num} ---")
    
    for item_num in range(1, items_per_receipt + 1):
        print(f"Item {item_num}")
    print()  
