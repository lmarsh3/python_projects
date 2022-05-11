# Alternate Exercise 3 - Print characters from a string that are present at an even idex number
# STEPS
# Python input() function to accept string from a user
# Next, iterate each character of a string using for loop and list() function.
# Use start = 0, step = 2 (pick even index numbers)
# in each iteration of a loop, print(i)

# input from user
my_string = input("Please enter string: ")
# original string
print(f'Original string: {my_string}')

# use list slicing
# convert string to list
# pick only even index characters
size = list(my_string)
for i in size[0::2]:
    print(i)
