#problem 3
import math

def problem3(n):
    primefactors = []
    primelist = []
    i = 2
    while n > i:
        if isprime(i) == True:
            if n % i == 0:
                primefactors.append(i)
                n = n/i
                print n
            else:
                i = i + 1
        else:
            i = i + 1
    primefactors.append(n)
    primefactors.sort()
    return primefactors
            
            
def isprime(p):
    if p == 2:
        return True
    elif p % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(p)),2):
        if p % i == 0:
            return False
    return True

print problem3(600851475143)
