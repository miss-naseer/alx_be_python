from datetime import datetime, timedelta

# Part 1 - Display Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # gets the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # formats it
    print("Current date and time:", formatted_date)

# Part 2 - Calculate Future Date
def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=days_to_add)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print("Future date:", formatted_future)
    except ValueError:
        print("Please enter a valid number of days.")

# Calling the functions
display_current_datetime()
calculate_future_date()
