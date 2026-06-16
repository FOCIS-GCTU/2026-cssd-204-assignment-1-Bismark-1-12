# File: zeller.py
# Description: <A program that calculates the day of the week>
# Assignment Number: 5 
# 
# Name: Bismark Anakwa Kwadwo
# SID:  2425403907
# Email: mcriches061@gmail.com
# Grader: AUGUSTUS BUCKMAN
# 
# On my honor, Bismark , this programming assignment is my own work
# and I have not provided this code to any other student.

# Step 1: Request inputs from the user
month_input = input("Enter the month (for example, January, February, etc.): ")
day_in_month = int(input("Enter the day (an integer): "))
year = int(input("Enter the year (an integer): "))

# Step 2: Map the month string to its specific algorithm number
if month_input == "January":
    month_number = 13
elif month_input == "February":
    month_number = 14
elif month_input == "March":
    month_number = 3
elif month_input == "April":
    month_number = 4
elif month_input == "May":
    month_number = 5
elif month_input == "June":
    month_number = 6
elif month_input == "July":
    month_number = 7
elif month_input == "August":
    month_number = 8
elif month_input == "September":
    month_number = 9
elif month_input == "October":
    month_number = 10
elif month_input == "November":
    month_number = 11
elif month_input == "December":
    month_number = 12

# Step 3: Adjust the year for January and February
if month_number == 13 or month_number == 14:
    year = year - 1

# Step 4: Perform Zeller's Congruence calculations using floor division (//)
variation_in_days_per_month = (13 * (month_number + 1)) // 5
leap_year_days = (year // 4) + (year // 400)
century_days = year // 100

total_days = day_in_month + variation_in_days_per_month + year + leap_year_days - century_days
day_of_week_numeric = total_days % 7

# Step 5: Convert the numeric day of the week to its string name
if day_of_week_numeric == 0:
    day_name = "Saturday"
elif day_of_week_numeric == 1:
    day_name = "Sunday"
elif day_of_week_numeric == 2:
    day_name = "Monday"
elif day_of_week_numeric == 3:
    day_name = "Tuesday"
elif day_of_week_numeric == 4:
    day_name = "Wednesday"
elif day_of_week_numeric == 5:
    day_name = "Thursday"
elif day_of_week_numeric == 6:
    day_name = "Friday"

# Step 6: Display the final result
print("The day of the week is " + day_name + ".")