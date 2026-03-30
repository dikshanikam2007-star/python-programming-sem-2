# ATM withdrawal system handles insufficient balance.
"""
Created on Mon Mar 30 15:34:03 2026

@author: DIKSHA
"""

def atm_withdrawal(balance, amount):
    print(f"Current Balance: ${balance}")
    print(f"Attempting to withdraw: ${amount}")
    
    try:
        if amount > balance:
            raise ValueError("Insufficient balance for this transaction.")
        
        balance -= amount
        print(f"Transaction successful! Remaining balance: ${balance}")
        
    except ValueError as e:
        print(f"Transaction Failed: {e}")
        
    finally:
        print("Thank you for using our ATM services. Please take your card.")

atm_withdrawal(500, 600)
