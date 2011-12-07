#p23
import pelib
import time


def p23():
    #find perfect divisors up to 28123
    #find divisors of each number
    perfectdivisors = []
    for i in range(28124):
        if sum(divisors(i)) > i:
            perfectdivisors.append(i)
    #for i in range(28124):
    #return len(perfectdivisors)
    sumabundants = []
    for i in range(0,len(perfectdivisors)):
        j = 0
        while (perfectdivisors[i]+perfectdivisors[j]) < 28124:
            sumabundants.append(perfectdivisors[i]+perfectdivisors[j])
            j = j + 1
    sumabundants.sort()
    sumabundants = pelib.remove_dupes(sumabundants)
    temp = 0
    for i in range(1,28124):
        if i in sumabundants:
            pass
        else:
            temp += i
    return temp
    
def divisors(n):
    divs = []
    for i in range(1,n):
        if n % i == 0:
            divs.append(i)
    return divs

ptime = 0
ptime -= time.clock()
print p23()
ptime += time.clock()
print ptime
