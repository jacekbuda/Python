# -*- coding: utf-8 -*-

num1, operator, num2 = input('Enter calculation ').split()

num1 = int(num1)
num2 = int(num2)

if operator == ('+'):
    print('{} + {} = {}'.format(num1, num2, num1+num2))
elif operator == ('-'):
    print('{} - {} = {}'.format(num1, num2, num1 - num2))
elif operator == ('*'):
    print('{} * {} = {}'.format(num1, num2, num1 * num2))
elif operator == ('/'):
    print('{} / {} = {}'.format(num1, num2, num1 / num2))
elif operator == ('%'):
    print('{} % {} = {}'.format(num1, num2,num1 % num2))
else:
    print('Operator not found, try another one')
