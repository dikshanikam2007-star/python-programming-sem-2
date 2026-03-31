# A library dictionary stores book name and price. Update book price.
"""
Created on Mon Mar  9 15:51:47 2026
@author: DIKSHA 
"""

library_catalog = {
    "The Great Gatsby": 450,
    "1984": 300,
    "The Hobbit": 550,
}
print(f"Old Price of 1984: ₹{library_catalog['1984']}")
library_catalog["1984"] = 325
library_catalog["Atomic Habits"] = 400
print(f"Updated Catalog: {library_catalog}")
