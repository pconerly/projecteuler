#project euler p10
import math
import time

def isprime(p):
    if p % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(p))+2,2):
        if p % i == 0:
            return False
    return True

def p10(n=2000000): #finds primes below a number
    ptime = 0
    ptime -= time.clock()
    sum = 2
    for i in range(3,n):
        if isprime(i):
            sum += i
    ptime += time.clock()
    print ptime
    return sum

print p10()
