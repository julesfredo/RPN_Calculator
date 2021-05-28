# Author | Julian Salmon
# Date | 05/17/2021

# This is a sample Python script.

operators = ['+','-','*','/','^']

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def calculate(expression):
    stack = []
    print(expression)
    for token in expression:
        if token in operators:
            print(f'operator: {token}')
            #read and calculate
            y = stack.pop()
            x = stack.pop()
            #evaluate operands based on operator (token)
            if token == '+':
                result = x + y
            elif token == '-':
                result = x - y
            elif token == '*':
                result = x * y
            elif token == '/':
                result = x / y
            elif token == '^':
                result = x ^ y
            stack.append(result)
        else:
            print(f'operand: {token}')
            stack.append(float(token))

        if len(stack) == 1:
            print(f'ans: {stack}')

def main():
    expression = input('>> ')
    calculate(expression.split())

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
