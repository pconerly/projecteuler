#p45
import math

def trinum(n):
    return n*(n+1)*0.5

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

def istriangle(n):
    a = 0.5
    b = 0.5
    c = -1*n
    x = (-1*b + math.sqrt(math.fabs( (b)**2 - (4*a*c) ) ) )/(2*a)
    #y = (-1*b - math.sqrt(math.fabs( (b)**2 - (4*a*c) ) ) )/(2*a)
    #print x
    if int(x) == x:
        return True
    return False

def test():
    istriangle(40755)
    return

def ishexagonal(n):
    a = 2
    b = -1
    c = -1*n
    x = (-1*b + math.sqrt(math.fabs( (b)**2 - (4*a*c) ) ) )/(2*a)
    #y = (-1*b - math.sqrt(math.fabs( (b)**2 - (4*a*c) ) ) )/(2*a)
    #x = max(x,y)
    if int(x) == x:
        return True
    return False

def p45():
    i = 285 #the last number that fits all 3
    i += 1
    tri = trinum(i)
    while True:
        if ishexagonal(tri) and ispentagonal(tri):
            return i, trinum(i)
        #if istriangle(i):
        #    print "tri", i
        #if ispentagonal(i):
        #    print "         ", "pnt", i
        #if ishexagonal(i):
        #    print "         ","         ","hex", i
        i += 1
        tri = trinum(i)

#print test()
print p45()
