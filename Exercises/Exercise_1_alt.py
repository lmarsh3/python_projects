# Alternate Exercise # 1
# STEPS
# 1. Create Function that will take 2 numbers as parameters.
# 2. Next, inside a function, multiply two numbers and save their product in a product variable.
# 3. Next, use if condition to check if product is > 1000. If yes, return product.
# 4. Next, if sum, calculate the sum of those numbers and return in.


def mult_sum_func(num1, num2):
    product = num1 * num2

    if product > 1000:
        return product
    else:
        return num1 + num2

result = mult_sum_func(20, 30)
print(f'The result is {result}')

result = mult_sum_func(40, 30)
print(f'The result is {result}')
