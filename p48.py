#p48
#WARNING 0**0 == 1.  ^^ WTF mates.
def p48():
    total = 0
    for i in range(1,1001):
        total += i**i
    print total
    return str(total)[-10:]

print p48()
