# -*- coding: utf-8 -*-

#some simply functions[

#first
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()

    num1, num2 = int(num1), int(num2)

    return 'x = ' + str(num2 - num1)
print(solve_eq('x + 4 = 9'))

#second
def solve_eq2(equationn):
    num1, add, x, equal, num2 = equationn.split()

    num1, num2, = int(num1), int(num2)

    return 'x = ' + str(num2 -num1)
print(solve_eq2('2 + x = 9'))

#third
def mult_divide(num1, num2):
    if num1 > num2:
        return (num1 * num2), (num1 /num2)

mult, divide = mult_divide(5, 4)

print('5 * 4 =', mult)
print('5 / 4 =', divide)




