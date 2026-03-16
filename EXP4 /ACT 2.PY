#A shopping app stores product prices in a list. Find total bill.

"""
Created on Mon Mar 16 15:45:09 2026

@author: DIKSHA
"""
def calculate_total_bill(prices, tax_rate=0.05):
    # 1. Calculate the raw sum of all items
    subtotal = sum(prices)
    
    # 2. Calculate tax amount (e.g., 5%)
    tax_amount = subtotal * tax_rate
    
    # 3. Final total
    total_bill = subtotal + tax_amount
    
    return subtotal, tax_amount, total_bill

# --- Sample Cart ---
# Prices of items added to the shopping app
cart_items = [29.99, 9.50, 120.00, 45.00, 5.25]

sub, tax, final = calculate_total_bill(cart_items)

print(f"--- Checkout Summary ---")
print(f"Items in Cart: {len(cart_items)}")
print(f"Subtotal:      ${sub:,.2f}")
print(f"Tax (5%):      ${tax:,.2f}")
print(f"------------------------")
print(f"Total Bill:    ${final:,.2f}")
