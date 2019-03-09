# -*- coding: utf-8 -*-

age = int(input('Ile masz lat?\n'))
if ( age >= 18 ):
    print('Użytkownik pełnoletni')
if ( age > 100 ):
    print('200 lat')
else:
    print('Użytkownik niepełnoletni')
    print('Do 18. urodzin zostało ci:' , 18 - age , 'lat')
