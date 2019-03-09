# -*- coding: utf-8 -*-

sentence = "Kurs Pythona jest prosty i przyjemny."

#Podaj liczbę znaków wyżej podanego zdania
lenght = len(sentence)
print(lenght)

#Wyświetla znaki o podanych w zadaniu indeksach
print('Znak o indeksie 7 to:' , sentence[7])
print('Znak o indeksie 12 to:' , sentence[12])
print('Znak o indeksie 4 od końca to:' , sentence[-4])
print('Znak o indeksie  37 nie istnieje, ponieważ znaki liczymy od 0.\nCzyli od 0 do 36, ostatni znak to:', sentence[36])

#Wprowadza specjalnie błędy ortograficzne
sentence = sentence.replace('u', 'ó')
sentence = sentence.replace('h', 'ch')
print('Zdanie z błedami wygląda tak: {}'.format(sentence))

#Wyświetla słowo "prosty"
sentence = sentence.split()
print(sentence[3])
