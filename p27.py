#p27
def makeprimes(n):
    primes = []
    for i in range(n+1):
        if isprime(i):
            primes.append(i)
            #print i
    return primes

def isprime(n):
    '''check if integer n is a prime'''
    if n < 0:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    for x in range(3, int(n**0.5)+2,2):
        if n % x == 0:
            return False
    return True

def p27():
    a = -1000
    b = -1000
    maxcount = 0
    maxa = 0
    maxb = 0
    primes = makeprimes(3000)
    while a < 999:
        a += 1
        b = -1000
        while b < 999:
            b += 1
            n = 0
            count = 0
            while (n**2 + a*n + b) in primes:
                count += 1
                n += 1
            if count > maxcount:
                print "newmax", count, "a and b", a, b
                maxcount = count
                maxa = a
                maxb = b
    print maxa, maxb    
    return maxa*maxb

print p27()
#print len(makeprimes(3000))
        
