# -*- coding: utf-8 -*-

x = int(input('Podaj ile razy program ma sprawdzać  liczbę: '))
x = (x + 1)

for i in range(0, x):
    ja = int(i % 3)
    ca = int(i % 4)
    if ja == 0:
        print('Liczba {} jest wielokrotnością 3'.format(i))
    if ca == 0:
        print('Liczba {} jest wielokrotnością 4'.format(i))
    if (ja == 0) and (ca == 0):
        print('HURRA !, liczba {} jest wielokrotnością 3 jak i 4 !'.format(i))
    else:
        print('*')

