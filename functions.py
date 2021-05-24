from random import *

print('----------1----------')
# Helper Functions
# 1 --> Print Functions

# function: print_addition
#   parameters
#       a | integer | addend
#       b | integer | addend
#
#   return_value
#       none
#
#   description: prints the sum of a + b
def print_addition(a, b):
    print(f'{a} + {b} = {a + b}')


print_addition(randint(1, 100), randint(1, 100))


# 1
# Define the following functions:
#   - print_subtraction
#   - print_multiplication
#   - print_division
#
# You do not have to call with random numbers if you do not want to, though I encourage it.
def print_subtraction(a, b):
    print(f'{a} - {b} = {a + b}')

def print_multiplition(a, b):
    print(f'{a} * {b} = {a + b}')

def print_division(a, b):
    print(f'{a} / {b} = {a + b}')


# Helper Functions
# 2 --> Return Functions

# function: addition
#   parameters
#       a | integer | addend
#       b | integer | addend
#
#   return_value
#       a + b | integer | the sum of a and b
#
#   description: returns the sum of a + b
def addition(a, b):
    return a + b


num1, num2 = randint(1, 100), randint(1, 100)
result = addition(num1, num2)
print(f'{num1} + {num2} = {result}')


# 2
# Define the following functions:
#   - subtraction
#   - multiplication
#   - division
#
# You do not have to call with random numbers if you do not want to, though I encourage it.

def main():
    list = input()
    for i in range(len(list)):
        token = list.pop()
        if token == '+' or token == '-' or token == '*' or token == '/' or token == '^':
            # convert token
            x = list.pop()
            y = list.pop()
            if token == '+':
                result = y + x
            if token == '-':
                result = y - x
            if token == '*':
                result = y * x
            if token == '/':
                result = y / x
            if token == '^':
                result = y ^ x

            list.push(result)
        if int(token):
            list.push(token)

        if len(list) == 1:
            print(list)
        else:
            print('incorrect number of operands / operators')

