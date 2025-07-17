# Instructions:

# Prompt User for a Number:

# Ask the user to input a number for which they want to see the multiplication table: Enter a number to see its multiplication table:.
# Save it in a variable name number
# Generate and Print the Multiplication Table:

# Use a for loop to iterate through the numbers 1 to 10.
# For each iteration, calculate the product of the user’s number and the iterator (the current number in the loop from 1 to 10).
# Print each line of the multiplication table in the format: “X * Y = Z”, where X is the user’s number, Y is the current number in the loop, and Z is the product.


number = int(input('Enter a number to see its multiplication table: '))

for num in range(1, 11):
 result = number * num
 print(f"{number} * {num} = {result}")