#Prevent cash when dividing bill among zero people.
"""
Created on Mon Mar 30 15:51:35 2026

@author:DISKHA
"""

def split_bill():
    print("--- Restaurant Bill Splitter ---")
    
    try:
     total_bill = float(input("Enter the total bill amount: rupees$"))
     num_people = int(input("Enter the number of people: "))

     if num_people == 0:
         raise ZeroDivisionError("You cannot split a bill among zero people.")
     if num_people < 0:
         raise ValueError("The number of people cannot be negative.")

     share = total_bill / num_people
     print(f"Each person should pay: rupees${share:.2f}")

    except ZeroDivisionError as e:
        print(f"Math Error: {e}")

    except ValueError as e:
        print(f"Input Error: Please enter valid numbers. ({e})")

    finally:
        print("Calculation attempt finished. Please see the host for the final receipt.")

split_bill()
