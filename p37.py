#p37
import pelib

def p37():
    b = True
    count = 0
    total = 0
    for i in range(10,1000000):
        if pelib.isprime(i):
            b = True
            #print
            #print i
            for j in range(0,len(str(i))):
                if pelib.isprime(int(str(i)[j:])) and pelib.isprime(int(str(i)[:j+1])):
                    #print str(i)[j:], str(i)[:j+1]
                    pass
                else:
                    b = False
                    #print "failed"
            if b:
                count += 1
                total += i
                #print
                print count, i, total
                #for j in range(0,len(str(i))):
                #    print str(i)[j:], str(i)[:j+1]
    return total

print p37()
                
