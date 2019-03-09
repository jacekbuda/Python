# -*- coding: utf-8 -*-
#ten natomiast oblicza twoje BMI, jak nie wiesz wygogluj sobie...lol

print("Witaj użytkowniku!")
print("podaj swoją wagę w kg: ")
waga = int(input())
print("POdaj swój wzrost w metrach: ")
wzrost = float(input())

BMI= waga/wzrost**2
print("Twoje BMI wynosi: ",BMI)
