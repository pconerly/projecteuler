#p14 11/23/2010
def p14():
    bigstartnum = 0
    bigcount = 0
    i = 0
    while i < 1000000:
        i += 1
        tempcount = iterate(i)
        if i % 10000 == 0:
            print i
        if tempcount > bigcount:
            bigstartnum = i
            bigcount = tempcount
    return bigstartnum

def iterate(n):
    count = 0
    while True:
        if n == 1:
            return count
        n = hotpo_next(n)
        count += 1

def hotpo_next(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1

print p14()
