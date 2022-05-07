# Exercise # 1 - Calculate the multiplication and sum of 2 numbers.
#                Display product if > 1000 or display sum if < 1000


number1 = int(input('Please enter 1st number: '))
number2 = int(input('Please enter 2nd number: '))

if (number1 * number2) > 1000: # Check to see if the product of 2 numbers is greater than 1000
    print(f'The result is: {number1 * number2}')
else:
    print(f'The result is: {number1 + number2}')