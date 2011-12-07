#p51
import pelib
import time

def p51():
    num = 0
    while True:
        num += 1
        if num % 1000 == 0:
            print num
        if pelib.isprime(num):

            for i in range(3): #i may be doing some repetative calculations here
                #hopefully it won't be much
                has = has012(num, str(i))
                if has != False:
                    tally = 1
                    for j in range(i+1, 10):
                        if pelib.isprime(perm(num, str(i), str(j))):
                            tally += 1
                    if tally == 8:
                        print "found it!!!" , num
                        print "found the smallest prime in a eight prime value family"
                        return num
                    if tally == 7 and i > 0:
                        print "potential alternative condition", num


def has012(num, or012): #if num has 0,1,2 then it returns which positions they #are in
    digits = list(str(num))
    positions = []
    if or012 in digits:
        i = 0
        while len(digits) > 0:
            if digits[0] == or012:
                positions.append(i)
                i += 1
                digits.pop()
            return positions
    else:
        return False

def perm(num, or012, replacement):
    digits = list(str(num))
    new = ''
    for i in range(len(digits)):
        if digits[i] == or012:
            new = new + replacement
        else:
            new = new + digits[i]
    return int(new)
        
ptime = 0
ptime -= time.clock()
print p51()
ptime += time.clock()
print ptime
