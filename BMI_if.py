# -*- coding: utf-8 -*-

weight = int(input('Podaj swoja masę ciała [kg]:\n'))
height = float(input('Podaj swój wzrost [cm]:\n'))
BMI = weight / (height/100) ** 2
print('Twoje BMI wynosi: {:.2f}'.format(BMI))

if ( BMI <= 18.5 ):
    print('Masz niedowagę !')
elif ( 18.5 < BMI <= 24):
    print('Yuuupi, twoja waga jest w normie')
elif ( 24 < BMI <= 26.5):
    print('Uuu, masz lekką nadwagę')
else:
    print('Niedobrze, masz nadwagę')
    if ( 30 < BMI <=35  ):
        print( 'A także u ciebie niestety występuje otyłość I stopnia')
    elif ( 35 < BMI <=40 ):
        print('A także u ciebie występuje otyłość II stopnia')
    else:
        print('A także u ciebie występuje otyłość III stopnia')
