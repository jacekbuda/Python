# -*- coding: utf-8 -*-

age = int(input('Enter your age: '))
if (age >= 1) and (age <= 18):
    print('Important birthday !')
elif (age == 21) or (age == 50):
    print('Important birthday !')
elif not (age < 65):
    print('Important birthday !')
else:
    print('Not important')
