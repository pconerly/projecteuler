#p44
import math

def ispentagonal(n):
    a = 1.5
    b = -0.5
    c = -1*n
    x = (-1*b + math.sqrt(math.fabs( (b)**2 - (4*a*c) ) ) )/(2*a)
    #y = (-1*b - math.sqrt(math.fabs( (b)**2 - (4*a*c) ) ) )/(2*a)
    #x = max(x,y)
    if int(x) == x:
        return True
    return False

def pent(n):
    #print n,"this is n", n*(3*n -1)*0.5
    return n*(3*n -1)*0.5

def p44():
    minD = 10000000000
    pents = []
    for i in range(1,1000):
        pents.append(pent(i))
    for a in range(1,10000):
        for b in range(a,10000):
            if ispentagonal(pent(a) + pent(b)):
                #print "small hit", a, b
                if ispentagonal(math.fabs(pent(a) - pent(b))):
                    print "hit", a, b
                    if minD > math.fabs(pent(a) - pent(b)):
                        minD = math.fabs(pent(a) - pent(b))
    return minD

def test():
    for i in range(1,100):
        print i, ispentagonal(i)
    return

def test3():
    for i in range(1, 100):
        print ispentagonal(math.fabs(pent(i)))


#print test3()
print p44()
