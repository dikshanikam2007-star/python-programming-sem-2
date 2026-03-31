# A class attendance system stores roll numbers in sets. Find students present in both classes.
"""
Created on Mon Mar 16 15:56:24 2026
@author: DIKSHA
"""

math_attendance = {101, 102, 105, 108, 110}
science_attendance = {102, 103, 108, 112, 115}

both_present = math_attendance & science_attendance
# both_present = math_attendance.intersection(science_attendance)

print(f"Students in both classes: {both_present}")
