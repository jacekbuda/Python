# -*- coding: utf-8 -*-

#ten skurwesyn oblicza dzienne zapotrzebowanie kaloryczne dla chłopa,
#ale dla pizdeczki coś się znajdzie


#Lista trybów pracy, stylu życia
list = [
'Praca siedząca, brak dodatkowej aktywności fizycznej',
'Praca niefizyczna, mało aktywny tryb życia',
'Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu',
'Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu',
'Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu'
]

#Powitanie uzytkownika
print("Siema mordeczko !")
name = input('Podaj imię: ')
name = name.capitalize()
print('{} , ten program umożliwi Ci obliczenie dziennego zapotrzebowania kalorycznego ! Jedziemy !'.format(name))



#polecenia zapisujące dane potrzebne do obliczeń
waga = float(input("Podaj ile ważysz [kg]: "))
wzrost = float(input("Podaj wzrost [cm]: "))
wiek = int(input("Podaj wiek: "))
wsp = 0

print('Określ tryb życia, wybierz jedno:  ')

#pętla wypisująca na ekran wartośći z listy ( 'list' )
for i in list:
    print('*', i)

#polecenie proszące uzytkownika o dane potrzebne do
print('Wpisz rodzaj pracy(here): ')
work = input()

#zmianna z wartościa 'true', służy do sprawdzenia czy wystąpił błąd w poniższej funkcji warunkowej
is_well = True

#funkcja warunkowa decydująca o wartości współcczynnika 'wsp'
if work == 'Praca siedząca, brak dodatkowej aktywności fizycznej':
    wsp = 1.2
elif work == 'Praca niefizyczna, mało aktywny tryb życia':
    wsp = 1.4
elif work == 'Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu':
    wsp = 1.6
elif work == 'Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu':
    wsp = 1.8
elif work == 'Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu':
    wsp = 2.0
else:
    is_well = False
    print('Ups, coś poszło nie tak, sprubuj ponownie, proszę !')

# polecenie sprawdza czy imię kończy się literą 'a', imię żeńskie czy męskie
last =  name.endswith('a')

#funkcja warunkowa decydująca o wartości współczynnia 'S'
if last is False:
    S = 5
else:
    S = -161

#finalne obliczania

if is_well == True:
    PPM = 10 * waga + 6.25  *wzrost  -5 * wiek + S
    output = float(PPM * wsp)
    print('Twoje dzienne zapotrzebowanie kalorycznie wynosi: {:.2f} kcal'.format(output))
else:
    print('Z powodu wystąpienią błędu nie możemy obliczyć dziennego zapotrzebowania dla Ciebie, za utrudnienia przepraszamy :(')
