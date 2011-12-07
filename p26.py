#p26

def p26(n):
    maxd = 0
    maxcycle = 0
    for i in range(2,n):
        rem = []
        cur = 10 % i
        marker = False
        #print "first cur", cur
        while marker == False:
            if cur in rem:
                #print "cur in rem", cur, rem
                if len(rem) > maxcycle:
                    maxcycle = len(rem)
                    maxd = i
                marker = True
            rem.append(cur)
            cur = (cur*10 % i)
            #print "next cur", cur
        #print rem
    return maxd, maxcycle

print p26(1000)
