# -*- coding: utf-8 -*-

name = input('Podaj swoje imię\n')
surname = input('Podaj swoje nazwiko\n')
number = input('Podaj swój numer telefonu\n')

#Sprawdza czy imie, nazwisko zawierają tylko litery a numer tylko cyfry
print('Czy twoje imie zawiera tylko litery ?' , name.isalpha())
print('Czy twoje nazwisko zawiera tylko litery ?' , surname.isalpha())
print('Czy twój numer teleonu zawiera tylko cyfry ?', number.isdigit())

#Poprawia pierwsze litery imienia i nazwiska
print('Czy twoje imię i nazwikso zaczyna się od dużej litery ?. Teraz już tak xD')
name = name.capitalize()
surname = surname.capitalize()
print('Poprawione imię i nazwisko:',name,surname)

#Usuwa z numeru niepotrzebne spacje i myślniki
number = number.replace(' ' , '')
number = number.replace('-' , '')
print('Poprawiony numer telefonu:',number)

#Sprawdza czy użytkownik jest płcią piękną xD
print('Użytkownik jest kobietą ?', name.endswith('a'))

personal = name + " " + surname + " " + number
print(personal)

print('Długość wynosi: {}' .format(len(personal)))

#od liczby długości PERSONAL odejmnuje liczbę SPACJI oraz numer telefonu
letters = len(personal) - personal.count(" ") - 9 
print(letters)
                
