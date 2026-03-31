#A shopping app stores product prices in a list. Find total bill.
"""
Created on Mon Mar 16 15:45:09 2026

@author: DIKSHA
"""
prices = [299.0, 49.5, 1200.0, 85.25, 310.0]
total_bill = 0
for price in prices:
    total_bill += price

print(f"Items in cart: {len(prices)}")
print(f"Total Bill Amount: ₹{total_bill:,.2f}")

