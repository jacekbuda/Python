# -*- coding: utf-8 -*-

a = int(input('Podaj jeden bok:  '))
b = int(input('Podaj drugi bok:  '))
c = int(input('Podaj trzeci bok: '))


if ( a > b ):
    temp = a
    a = b
    b = temp
if ( a > c ):
    temp = a
    a = c
    c = temp
if ( b > c ):
    temp = b
    b = c
    c = temp

print('Boki które podałeś:', a, b, c )
triangle = False 

if ( a + b > c):
    print('Można utworzyć taki trójką')
    triangle = True
else:
    print('Ojoj, z tego to trójkąta nie bedzie xD')

if ( triangle and a**2 + b**2 == c**2):
    print('Tak, to jest trójkąt pitagorejski')
    if ( a/3 == b/4 == c/5 ):
        print('I to jesze egipski !')
elif ( triangle ):
    print('To z pwenością trójkąt ale kij wie jaki, sorka :*')
    
