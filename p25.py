#p25
def p25():
    prev = 1
    cur = 1
    count = 2
    while len(str(cur)) < 1000:
        cur, prev = cur + prev, cur
        count += 1
        #print cur, prev
    print prev, len(str(prev))
    print len(str(cur))
    print count, "count!"
    return cur

print p25()
