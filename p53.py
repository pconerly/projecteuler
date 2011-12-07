#problem 53
import math

count = 0

for n in xrange(1, 101): #could be until 23
    last = 0
    r = 1
    while r < n:
        last = math.factorial(n) /(math.factorial(r) * (math.factorial(n-r)))
        r += 1
        if last > 1000000:
            count += 1
            print("found one!", count, "n", n, "r", r)

print count
