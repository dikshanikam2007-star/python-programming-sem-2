#A teacher stores marks of students in a list. Find average and topper marks.
"""
Created on Mon Mar 16 15:40:11 2026
@author: DIKSHA
"""

marks = [85, 92, 78, 95, 88, 70, 99]
topper_marks = max(marks)

total_sum = sum(marks)
num_students = len(marks)
average_marks = total_sum / num_students

print(f"Total Students: {num_students}")
print(f"Topper Marks: {topper_marks}")
print(f"Average Marks: {average_marks:.2f}")
