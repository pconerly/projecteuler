import pelib
import time

def p12():
    trinum = 1
    count = 1
    while divisors(trinum) <= 500:
        #if count % 1000 == 0:
            #print count, trinum, "divisors", divisors(trinum)
        count += 1
        trinum += count
    return trinum

def divisors(n):
    factors = pelib.prime_factors(n)
    temp = [0]*factors[-1]
    div = 1
    #get multiples of divisors
    for i in range(len(factors)):
        temp[factors[i]-1] += 1
    #find divisors
    for i in range(len(temp)):
        if temp[i] > 0:
            div *= (temp[i]+1)
    return div

ptime = 0
ptime -= time.clock()
print p12()
ptime += time.clock()
print ptime
#print divisors(30)

