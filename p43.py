#p43

def ispandigital(n): #pandigital for 0-9
    n = str(n)
    if len(n) != 10:
        return False
    digits = []
    for i in range(len(n)):
        digits.append(n[i])
    digits.sort()
    #print digits
    for j in range(0,10):
        if j != int(digits[j-1]):
            #print "will return false",
            return False
    return True

def lexpos_to_num(lexpos, digits = 9):
    digits += 1
    d = range(digits)
    new = []
    for i in range(digits):
        new.append(d[lexpos[i]])
        d.pop(lexpos[i])
    return new


def incr_lexpos(lexpos):
    if lexpos == [9, 8, 7, 6, 5, 4, 3, 2, 1]:
        return False
    lexpos[-1] += 1
    length = len(lexpos)
    #print "length", length
    for i in range(0,10):
        #print length - i
        if lexpos[length-(i+1)] > i:
            lexpos[length-(i+1)] -= 1
            lexpos[length-(i+2)] += 1
            for j in range(length-(i+1), length):
                lexpos[j] = 0
            
    return lexpos
    
def test():
    lexpos = [0]*10
    n = lexpos_to_num(lexpos)
    print lexpos
    while lexpos:
        lexpos = incr_lexpos(lexpos)
        n = lexpos_to_num(lexpos)
        print lexpos
    return n

def test2():
    lexpos = [0]*10
    n = lexpos_to_num(lexpos)
    print lexpos
    for i in range(1000):
        lexpos = incr_lexpos(lexpos)
        n = lexpos_to_num(lexpos)
        print lexpos
    return n

def test3():
    for i in range(1, 100):
        print ispentagonal(math.fabs(pent(i)))

def list_to_num(l):
    string = ''
    for i in range(len(l)):
        string += str(l[i])
    return int(string)

def p43():
    primes = [2,3,5,7,11,13,17]
    total = 0
    lexpos = [0]*10
    n = lexpos_to_num(lexpos)
    i = 0
    while i <  3628800:
        #if ispandigital(n):
        tag = True
        for j in range(7):
            if int(str(n[1+j]) + str(n[2+j])+ str(n[3+j])) % primes[j] != 0:
                tag = False
        if tag:
            total += list_to_num(n)
            print i, list_to_num(n), total
        lexpos = incr_lexpos(lexpos)
        n = lexpos_to_num(lexpos)
        i += 1
    return total

print test3()

#print p43()


