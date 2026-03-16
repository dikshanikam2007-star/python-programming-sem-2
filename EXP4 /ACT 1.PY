#A teacher stores marks of students in a list. Find average and topper marks.
"""
Created on Mon Mar 16 15:40:11 2026

@author: DIKSHA
"""

def analyze_marks(student_marks):
    # 1. Check if the list is empty to avoid errors
    if not student_marks:
        return "No marks recorded."

    # 2. Calculate Total and Average
    total_marks = sum(student_marks)
    count = len(student_marks)
    average = total_marks / count

    # 3. Identify Topper and Lowest marks
    topper = max(student_marks)
    lowest = min(student_marks)

    return average, topper, lowest

# --- Sample Data ---
# Marks for a class of 8 students
marks_list = [85, 92, 78, 95, 88, 70, 99, 82]

avg, top, low = analyze_marks(marks_list)

print(f"--- Class Performance Report ---")
print(f"Total Students: {len(marks_list)}")
print(f"Average Score: {avg:.2f}")
print(f"Topper Score: {top}")
print(f"Lowest Score: {low}")
