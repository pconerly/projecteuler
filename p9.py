import math

def problem9():
    squarenum = []
    
    for i in range(1, 500):
        squarenum.append(i**2)
    
    for a in range(1,500):
        for b in range(1,500):
            if (a**2 + b**2 ) in squarenum:
                if a + b + int(math.sqrt(a**2 + b**2)) == 1000:
                    return a * b * int(math.sqrt(a**2 + b**2))

print problem9()
