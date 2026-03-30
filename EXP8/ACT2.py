#Handle invalid age input in registration form.
"""
Created on Mon Mar 30 15:46:37 2026

@author: DIKSHA
"""

def register_user(age_input):
    print(f"--- Processing Registration for Age: {age_input} ---")
    
    try:
        age = int(age_input)
        
        if age < 18:
            raise ValueError("Registration failed: You must be at least 18 years old.")
        if age > 120:
            raise ValueError("Registration failed: Please enter a valid age (max 120).")
            
        print(f"Success! Age {age} is verified. Proceeding to account creation...")

    except ValueError as e:
        print(f"Input Error: {e}")
        
    finally:
        print("Registration session closed. Returning to home screen.")

register_user("25")    
register_user("12")  
register_user("abc")  
