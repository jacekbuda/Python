# -*- coding: utf-8 -*-

def silnia(n):

    w = 1
    i = 1
    if n == 0:
        print(w)
    else:
        while i <= n:
            w = w * i
            i += 1
    print(w)

silnia(21)

