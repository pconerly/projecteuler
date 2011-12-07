#p47
import pelib

def p47():
    i = 0
    while True:
        i += 1
        temp = pelib.remove_dupes(pelib.prime_factors(i))
        if len(temp) == 4:
            count += 1
            if count == 4:
                return (i - 3)
        else:
            count = 0

print p47()
