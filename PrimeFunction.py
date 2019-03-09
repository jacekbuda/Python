# -*- coding: utf-8 -*-

#looking for primes function
def isprime(num):
    for i in range(2, num):
        if ( num % i) == 0:
            return False

    return True

def getprimes(max_number):

    list_of_primes = []

    for num in range(2, max_number):
        if isprime(num):
            list_of_primes.append(num)

    return list_of_primes

max_num_to_check = int(input('Search for Primes up to : '))

list_of_primes = getprimes(max_num_to_check)

for jack in list_of_primes:
    print(jack)