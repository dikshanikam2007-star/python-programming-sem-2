# A ticket booking system repeats seat display pattern using loops.
"""
Created on Mon Mar 16 15:35:20 2026

@author: User
"""

def display_seating(rows, seats_per_row):
    # Column Headers (Seat numbers)
    print("      ", end="")
    for s in range(1, seats_per_row + 1):
        print(f" {s:2} ", end="")
    print("\n" + "   " + "-" * (seats_per_row * 4 + 4))

    # Row Generation
    for r in range(rows):
        # Convert index to Row Letter (0=A, 1=B, etc.)
        row_label = chr(65 + r)
        print(f"Row {row_label} |", end="")
        
        for s in range(1, seats_per_row + 1):
            # Simulation: Mark seat B3 as booked
            if row_label == 'B' and s == 3:
                print(" [X]", end="")
            else:
                print(" [ ]", end="")
        
        # New line after each row is complete
        print()

# Generate a 5-row, 8-seat theater map
display_seating(5, 8)
