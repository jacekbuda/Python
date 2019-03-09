# -*- coding: utf-8 -*-
szer = 75
print("*" * szer)
jednostka = float(input("Podaj długość w [cm]\n"))
jwm = jednostka/100
jwc = jednostka/2.54
print("Podana przez ciebie długość w calach wynosi {:.2f} cala a w metrach {}m" .format(jwc,jwm))

jednostka2 = float(input("Podja wagę w [kg]\n"))
jwf = jednostka2/0.453
print("Waga w funtach to {:.2f}" .format(jwf))

