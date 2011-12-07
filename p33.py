#p33
import pelib

def p33():
    curious = []
    for a in range(10,98):
        for b in range(a+1,100):
            for i in range(2):
                ta = [str(a)[0], str(a)[1]]
                tb = [str(b)[0], str(b)[1]]
                if ta[i] in tb:
                    if int(ta[i]) != 0:
                        #print "test", a, b, ta, tb
                        tb.pop(tb.index(ta[i]))
                        ta.pop(i)
                        
                        if int(tb[0]) != 0:
                            if a/float(b) == float(ta[0])/float(tb[0]):
                                print "a & b", a, b
                                print "ta & tab", float(ta[0]),float(tb[0])
                                print a/float(b), float(ta[0])/float(tb[0])
                                print
                                curious.append([a,b])
    cnum = 1
    cden = 1
    for i in range(len(curious)):
        cnum *= curious[i][0]
        cden *= curious[i][1]
    print cnum, cden
    factors = [2,2,2,2,2,7,7,13,19]
    for i in range(len(factors)):
        cnum = cnum / factors[i]
        cden = cden / factors[i]
    print cnum, cden
    return

"""
manually find what to devide them by
2,2,2,2,2,7,7,13,19
"""
p33()

def test():
    count = 0
    for a in range(10,98):
        for b in range(a+1,100):
            count += 1
    return count

#print test()
