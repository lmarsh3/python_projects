# Exercise 2 - Print the sum of the current number and the previous number
# STEPS
# 1. Create a variable called previous_num and assign it to 0
# 2. Iterate the first 10 numbers one by one using for loop and range() function
# 3. Next, display the current number (i), previous number, and the addition of both numbers in each iteration of the loop.
#    At last, change the value previous number to current number (previous_num = i)

previous_num = 0

print('Printing current and previous number sum in a range(10)')

# range of 10. Similar to range(1, 11)
for i in range(10):
    print(f'Current Number {i} Previous Number {previous_num} Sum: {previous_num + i} ')
    previous_num = i