# -*- coding: utf-8 -*-
#ten skurwesyn oblicza dzienne zapotrzebowanie kaloryczne dla chłopa a nie pizdeczki
#wzór dla chłopów a nie jakiś pizdeczek, ta jeest

print("Siema mordeczko")

waga = float(input("Podsaj ile ważysz w [kg]:\n"))
wzrost = float(input("Podaj wzrost w [cm]:\n"))
wiek = int(input("Podaj wiek:\n"))
S = 5

PPM = 10*waga+6.25*wzrost-5*wiek+S
print("Twoej dzienne zapotrzebowanie kalorycznie wynosi:",PPM * 1.6)

