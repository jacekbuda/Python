# -*- coding: utf-8 -*-

a = 33
b = 101.5
c = 11

if ( a > b ) and ( a > c ):
    max = a
elif ( b > a ) and ( b > c ):
    max = b
else:
    max = c

print(max)


if ( a < b ):
    temp = a
    a = b
    b = temp
if ( a < c ):
    temp = a
    a = c
    c = temp
if ( b < c ):
    temp = b
    b = c
    c = temp


print(a , b , c )
