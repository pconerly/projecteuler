#p21
def p21(n):
    pairs = []
    amicable = []
    for i in range(n):
        pairs.append(divisors_sum(i))
    for i in range(n):
        #print i, pairs[i] #, pairs[pairs[i]]
        if pairs[i] < n:
            if pairs[pairs[i]] == i and i != pairs[i]:
                amicable.append(i)
                #print i, pairs[i]
    return sum(amicable)

def divisors_sum(n):
    div = []
    for i in range(1,int(n/2)+1):
        if n % i == 0:
            div.append(i)
    #print div
    return sum(div)

print p21(10000)
