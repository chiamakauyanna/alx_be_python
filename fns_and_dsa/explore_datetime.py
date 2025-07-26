# Current date and time: 2024-03-25 15:30:45
# Enter the number of days to add to the current date: 10
# Future date: 2024-04-04

from datetime import datetime, timedelta

def display_current_datetime():
  current_date = datetime.now()
  formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
  print('Current date and time:', formatted_date)
  return current_date

number_of_days = int(input('Enter the number of days to add to the current date: '))

def calculate_future_date():
  future_date = display_current_datetime() + timedelta(days=number_of_days)
  print('Future date:', future_date.strftime('%Y-%m-%d'))

calculate_future_date()

