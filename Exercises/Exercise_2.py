# Exercise 2 - Print the sum of the current number and the previos number
# STEPS
# 1. Create a variable called previous_num and assign it to 0
# 2. Iterate the first 10 numbers one by one using for loop and range() function

previous_num = 0

print('Printing current and previous number sum in a range(10)')

# This is partially working. issue when printing previous number and sum during first iteration. Both -1
for previous_num in range(0, 10):
    print(f'Current Number {previous_num} Previous Number {previous_num - 1} Sum: {previous_num + previous_num -1} ')