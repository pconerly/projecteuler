#p41
import pelib
import math

def lexpos_to_num(lexpos, digits = 9): #for 1-n
    digits += 1
    d = range(1,digits) #1 to 9
    new = []
    for i in range(1,digits):
        new.append(d[lexpos[i-1]])
        d.pop(lexpos[i-1])
    return new

def incr_lexpos(lexpos, n):
    lexpos[-1] += 1
    length = len(lexpos)
    #print "length", length
    for i in range(0,n):
        #print length - i
        if lexpos[length-(i+1)] > i:
            lexpos[length-(i+1)] -= 1
            lexpos[length-(i+2)] += 1
            for j in range(length-(i+1), length):
                lexpos[j] = 0
            
    return lexpos
    
def list_to_num(l): #works for any n
    string = ''
    for i in range(0,len(l)):
        string += str(l[i])
    return int(string)

def p41(n):
    lexpos = [0]*n
    for i in xrange(math.factorial(n)):
        lexpos = incr_lexpos(lexpos, n)
        if pelib.isprime(list_to_num(lexpos_to_num(lexpos, n))):
            print list_to_num(lexpos_to_num(lexpos, n))
    return

for i in range(2,8):
    p41(i)
