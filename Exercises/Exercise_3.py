# Exercise 3 - Print characters from a string that are present at an even idex number
# STEPS
# Python input() function to accept string from a user
# Next, iterate each character of a string using for loop and range() function.
# Use start = 0, stop = string length - 1, step = 2 (the step is 2 because we only want even index numbers)
# in each iteration of a loop, use []

# input from user
my_string = input("Please enter string: ")
# original string
print(f'Original string: {my_string}')
# length of entire string
size = len(my_string)

# iterate each character of a string
# start: 0 because of the start of the string
# stop: size because the index starts with 0
# step: 2 to access each index by 2 [0], [2], [4]
for i in range(0, size, 2):
    print (f'index[{i}] : {my_string[i]}')
