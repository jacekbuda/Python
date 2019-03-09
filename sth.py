# -*- coding: utf-8 -*-

import random

def main(x,y):
    enter = input(print("Wanna play disc roll boi ? [y/n]"))

    # we don't want any entering's errors ? Don't we ?
    enter.upper()

    while enter == "YES" or "Y":
        print("Rolling the dice" + points)

        print("Values are: \n")
        print(random.randint(x, y))
        print(random.randint(x, y))

    enter = input("Go again ? \n")
    a = random.randint(3, 15)
    points = "." *a

main()