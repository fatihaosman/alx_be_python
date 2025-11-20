import datetime

def display_current_datetime():
  current_date = datetime.now() 
  formatted_datetime = current_date .strftime("%Y-%m-%d %H:%M:%S")
  print("Current Date and Time:", formatted_datetime)

#Prompt the user to enter a number of days (as an integer).


def calculate_future_date():
  days_to_add = int(input("Enter number of days to add to current date: "))
  current_date = datetime.now()
  future_date = current_date + datetime.timedelta(days=days_to_add)
  formatted_future_date = future_date.strftime("%Y-%m-%d")
  print(f"Date after {days_to_add} days will be: {formatted_future_date}")