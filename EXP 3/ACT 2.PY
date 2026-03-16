#A school generates multiplication tables for students from 1 to 10.
"""
Created on Mon Mar 16 15:30:09 2026

@author:DIKSHA
"""

def generate_multiplication_table(limit=10):
    # Print the header row
    print("   ", end="")
    for i in range(1, limit + 1):
        print(f"{i:4}", end="")
    print("\n" + "-" * (limit * 5))

    # Generate rows
    for row in range(1, limit + 1):
        # Print the row label
        print(f"{row:2} |", end="")
        
        for col in range(1, limit + 1):
            # Calculate and format the product
            product = row * col
            print(f"{product:4}", end="")
        
        # Move to the next line after each row
        print()

# Run the function
generate_multiplication_table(10)
