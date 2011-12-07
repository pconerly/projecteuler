#p16 11/23/2010
#seriously, too easy.
def p16():
    digits = str(2**1000)
    print digits
    sum = 0
    for i in range(len(digits)):
        sum += int(digits[i])
    return sum

print p16()
