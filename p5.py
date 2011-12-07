#project euler problem 5
#what is the smallest number divisible by each of the numbers 1 to 20

import math


#this method finds the lowest common multiple 
def problem5():
    b = True
    test = True
    n = math.factorial(20)
    
    n = 148492554210000
    factors = []
    print n
    count = 0
    while b:
        for i in range(2,20): #tests to see if n is a multiple of answer
            test = True
            temp = n/i
            print 'n/' + str(i) + '=' + str(temp),
            for j in range(2,20): #tests all of the divisors
                if temp % j != 0:
                    print 'tested false at ' + str(j)
                    test = False
                    break
            if test == True: #n was a multi of answer
                n = temp
                count = count + 1
                factors.append(i)
                print "tested true"
                break
        if temp != n: #no changes
            print
            print "count", count
            print factors
            return n



#answer is 232792560
"""
>>> (2**4)*(3*2)*5*7*11*13*17*19
155195040
>>> (2**4)*(3**2)*5*7*11*13*17*19
232792560
"""

def print_divisors(n):
    print n
    for i in range(1,21):
        print i, n%i, n%i == 0

print_divisors(problem5())
#print_divisors(232792560)
