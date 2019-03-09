# -*- coding: utf-8 -*-

names = {
    'Jacek' : 'męskie',
    'Andrzej' : 'męskie',
    'Karol' : 'męskie',
    'Bartek' : 'męskie',
    'Marek' : 'męskie',
    'Patryk' : 'męskie',
    'Konrad' : 'męskie',
    'Jadwiga' : 'żeńskie',
    'Magda' : 'żeńskie',
    'Dorota' : 'żeńskie',
    'Monika' : 'żeńskie',
    'Aleksandra' : 'żeńskie',
    'Ewa' : 'żeńskie',
    'Helena' : 'żeńskie'
    }

name = (input('Podaj swoje imię:\n'))

if ( name in list(names.keys())):
    print( name , 'to imię' , names[name])
else:
    print('Nie znamy tego imienia !')
    print( 'Dodaj je do zbioru !, wpisz "m" jeśli to imię męskie a "ż" jeśli żenśkie')
    plec = input()
    if ( plec == 'ż'):
        names[name] = 'żeńskie'
    else:
        names[name] = 'męskie'
print('Imie zostało pmyślnie dodane do listy :)')
print(list(names.keys()))

        





    
    
