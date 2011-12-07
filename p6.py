#p6

def problem6(n):
    #sum of squares:
    susq = 0
    for i in range(1,n+1):
        susq = susq + i**2
    
    sqsu = 0
    for i in range(1,n+1):
        sqsu = sqsu + i
    sqsu = sqsu**2

    return sqsu - susq
    
print problem6(100)
