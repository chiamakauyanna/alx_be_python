# Instructions:

# Prompt for a Single Task:

# Ask the user to input a task description and save it into a task variable
# Prompt for the task’s priority (high, medium, low) and save it into a priority variable
# In a time_bound variable, Ask if the task is time-bound (yes or no)
# Process the Task Based on Priority and Time Sensitivity:

# Use a Match Case statement to react differently based on the task’s priority.
# Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
# Provide a Customized Reminder:

# Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
# A message should be ‘that requires immediate attention today!’

task = input('input a task description: ')
priority = input('what is the task priority? (high, medium, low): ').lower()
time_bound = input('is the task time bound? (yes or no): ').lower()

match priority:
  case 'high' | 'medium' | 'low':
    message = f'You have a task "{task}" with {priority} priority'
    if time_bound == 'yes':
      message += ', that requires immediate attention today!'
    print(message)
  case _:
     print("Invalid priority input.")
    