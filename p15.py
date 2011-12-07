#p15
def pascal(n):
    cur = [1]
    prev = [] #will get zeros on either side later
    for i in range(1,n):
        prev = [0] + cur + [0]
        cur = []
        for j in range(i+1):
            #print prev[i] + prev[i+1]
            cur.append(prev[j] + prev[j+1])
        print len(cur), cur
    return cur

def sqrlist(l):
    for i in range(len(l)):
        l[i] = l[i]**2
    return l

def p15():
    temp = pascal(21)
    temp = sqrlist(temp)
    temp = sum(temp)
    return temp

print p15()
