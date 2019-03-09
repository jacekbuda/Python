# -*- coding: utf-8 -*-

serials = {
    
    'Game of Thrones' : 7.5,
    'Naruto:Shippuden' : 9.6,
    'Tokyo Ghoul:Re' : 8.7,
    'Kanjo Real Girl':7.9,
    '13 Reasons Why': 8.9,
    'Bajeczki Kazahstańskie': 6.7
    }
print('*********************************************')
print(list(serials.keys()))
print('*********************************************')

watch = input('Jaki serial chcesz obejrzeć ?\n')

print('Serial {} otrzymał ocenę {}'.format(watch, serials[watch]))

add = input('Czy chcesz dodać inny serial do spisu ? Jeżeli tak wpisz tutaj nazwę\n')
ocena = input('Oceń serial:\n')

serials[add] = float(ocena)

print('*********************************************')
print(list(serials.keys()))
print('*********************************************')
