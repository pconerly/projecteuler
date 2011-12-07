#p34
import math

def p34(n):
    sumnums = 0
    for i in range(3,n):
        temp = str(i)
        facts = 0
        for j in range(len(temp)):
            facts += math.factorial(int(temp[j]))
        if facts == i:
            print i
            sumnums += i
    return sumnums            

print p34(1000000)
