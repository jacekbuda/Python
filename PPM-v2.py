# -*- coding: utf-8 -*-

def calculator():

    #lifestyles' list
    a = 'Sitting type of work; no additonal physical activity'
    b = 'Non-physical type of work; some, easy exercises '
    c = 'Easy kind of physical work; regular exercises (3-4 times week)'
    d = 'Physical work; regular exercises(min. 5 times week)'
    e = 'Pretty hard physical work; regular exercises(7 times week)'

    #'Hello' to user
    print('*'*75)
    print("Yoo, buddy !")
    name = input('Please, enter your name: ')
    name = name.capitalize()
    print('*'*75)
    print('{}, This program is helping you to calculate your daily caloric demand '.format(name))

    #gathering information for calculates
    weight = float(input("Enter your weight(do not even try to lie ;) )) [kg]: "))
    hight = float(input("Enter your hight [cm]: "))
    age = int(input("Enter your age: "))
    fct = 0


    print('Choose your lifestyle, conformable to ya :  ')

    print('a)', a)
    print('b)', b)
    print('c)', c)
    print('d)', d)
    print('e)', e)

    #asking for confirmation
    work = input('Confirm your lifestyle (choose a,b,c,d,e): ')
    str(work)
    print('*'*75)

    # 'if' function, decide to select correct factor
    if work == 'a':
        fct = 1.2
    elif work == 'b':
        fct = 1.4
    elif work == 'c':
        fct = 1.6
    elif work == 'd':
        fct = 1.8
    elif work == 'e':
        fct = 2.0
    else:
        is_well = False
        print('Ups, damm, sth went wrong!')

    #checking last letter (female or male)
    last =name.endswith('a')

    #'if' fucntion decide to select a correct S-factor
    if last is False:
        S = 5
    else:
        S = -161

    #Uff,finally some calculations:
    # value need to checking bugs,etc
    is_well = True
    if is_well == True:
        PPM = 10 * weight + 6.25  * hight  -5 * age + S
        output = float(PPM * fct)
        print('Your daily caloric demand is: {:.2f} kcal'.format(output))
        print('Hope your enjoy ;)')
    else:
        print('Cuz, there is a error, we can do anything :(')
    print('*'*75)

calculator()

