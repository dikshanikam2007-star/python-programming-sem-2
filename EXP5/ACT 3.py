#A shop inventory dictionary stores item name and quantity. Add new stock.
"""
Created on Mon Mar 16 15:59:52 2026
@author: DIKSHA
"""

inventory = {
    "Apples": 50,
    "Bread": 20,
    "Milk": 15
}
def update_stock(item, quantity):
    inventory[item] = inventory.get(item, 0) + quantity
    print(f"Updated {item}. New total: {inventory[item]}")
update_stock("Apples", 30)
update_stock("Eggs", 12)
print("\nFinal Inventory:", inventory)
