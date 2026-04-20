#To display the current date, time, and weekday using the datetime module
"""
Created on Mon Apr 20 15:00:08 2026

@author: DIKSHA
"""
import datetime
# Get current date and time
now = datetime.datetime.now()
# Print current date
print("Current Date:", now.strftime("%Y-%m-%d"))
# Print current time
print("Current Time:", now.strftime("%H:%M:%S"))

# Print current weekday
print("Weekday:", now.strftime("%A"))

