#p39
import math

def p39():
    squarenum = []
    int_tri = []
    
    for i in range(1, 500):
        squarenum.append(i**2)
    
    for a in range(1,500):
        for b in range(1,500):
            if (a**2 + b**2 ) in squarenum:
                if a + b + int(math.sqrt(a**2 + b**2)) <= 1000:
                    int_tri.append(a + b + int(math.sqrt(a**2 + b**2)))
    int_tri.sort()

    maxcount = 0
    maxp = 0
    count = 0
    for i in range(1,len(int_tri)):
        if int_tri[i] == int_tri[i-1]:
            count += 1
        elif count > maxcount:
            maxcount = count

            maxp = int_tri[i-1]
            print maxcount, maxp
        count = 0
    return maxp

print p39()
