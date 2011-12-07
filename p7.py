#problem 7

import math

def isprime(p):
    if p == 2:
        return True
    if p % 2 == 0 or p == 1:
        return False
    for i in range(3, int(math.sqrt(p))+2,2):
        if p % i == 0:
            return False
    return True

def problem7(n):
    i = 0
    primecount = 0
    while primecount != n:
        i = i + 1
        if isprime(i) == True:
            primecount = primecount + 1
            #print primecount, i
    return i

print problem7(10001)
