# A class attendance system stores roll numbers in sets. Find students present in both classes.
"""
Created on Mon Mar 16 15:56:24 2026

@author: DIKSHA
"""

def find_common_students(class_a, class_b):
    # The '&' operator finds elements present in both sets
    present_in_both = class_a & class_b
    
    # Alternatively: present_in_both = class_a.intersection(class_b)
    
    return sorted(list(present_in_both))

# --- Sample Data ---
# Roll numbers present in Morning Class
morning_class = {101, 102, 105, 108, 110, 112}

# Roll numbers present in Afternoon Class
afternoon_class = {102, 103, 108, 112, 115}

common = find_common_students(morning_class, afternoon_class)

print(f"Morning Attendance:   {morning_class}")
print(f"Afternoon Attendance: {afternoon_class}")
print(f"Students in Both: {common}")
print(f"Total Count:  {len(common)}")
