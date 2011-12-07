#p40
def p40():
    i = 1
    irr = '.'
    total = 1
    while len(irr) < 1001000:
        irr = irr + str(i)        
        i += 1
    total *= int(irr[1])
    print int(irr[1])
    total *= int(irr[10])
    print int(irr[10])
    total *= int(irr[100])
    total *= int(irr[1000])
    total *= int(irr[10000])
    total *= int(irr[100000])
    total *= int(irr[1000000])
    return total

print p40()
