# -*- coding: utf-8 -*-

#The program asks the user about names, separated by comma
#next, program shows on the screen greeting for everyone in list named names
names = input('Enter names, please separate them by comma: ').split(',')
names = list(names)
print(names)

for name in names:
    name = name.capitalize()
    print('Hello,' + name + '!')
