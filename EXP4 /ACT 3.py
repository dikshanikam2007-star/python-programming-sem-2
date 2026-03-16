# Reverse a customer feedback message.
"""
Created on Mon Mar 16 15:51:24 2026

@author: DIKSHA
"""

def reverse_feedback(message):
    # This reads the string from end to start with a step of -1
    return message[::-1]

# --- Sample Program ---
customer_msg = "The service was excellent!"
reversed_msg = reverse_feedback(customer_msg)

print(f"Original: {customer_msg}")
print(f"Reversed: {reversed_msg}")
