# -*- coding: utf-8 -*-

stan = float(input("Podaj stan początkowy konta w [zł]\n"))
procent = float(input("Podaj oprocentowanie roczne w [%]\n"))
lata = float(input("Podaj liczbe lat na lokacie\n"))

odst = stan*(procent/100)*lata
hajsik = stan+odst

print("Twoje {:.2f} zł przez {:.1f} lata na lokacie {:.1f} % urośnie do {:.2f} zł".format(stan, lata, procent, hajsik))
