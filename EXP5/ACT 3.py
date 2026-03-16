#A shop inventory dictionary stores item name and quantity. Add new stock.
"""
Created on Mon Mar 16 15:59:52 2026

@author: DIKSHA
"""

def update_inventory(inventory, item_name, added_quantity):
    # .get() allows us to find the current stock
    # If the item doesn't exist, it defaults to 0
    current_stock = inventory.get(item_name, 0)
    
    # Update the dictionary with the new total
    inventory[item_name] = current_stock + added_quantity
    
    print(f"Updated {item_name}: {inventory[item_name]} in stock.")
    return inventory

# --- Initial Inventory ---
shop_stock = {
    "Apples": 50,
    "Bread": 20,
    "Milk": 15
}

# --- Adding New Stock ---
# 1. Adding to existing item
update_inventory(shop_stock, "Apples", 30)

# 2. Adding a brand new product
update_inventory(shop_stock, "Eggs", 100)

print(f"\nFinal Inventory: {shop_stock}")
