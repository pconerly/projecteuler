#problem 2
def problem2():
    c = 0
    prev = 1
    cur = 2
    while cur <= 4000000:
        if cur % 2 == 0:
            c += cur
        prev, cur = cur, prev + cur
    return c

print problem2()
