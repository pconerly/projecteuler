#p36
import pelib

def p36():
    total = 0
    for i in range(1000000):
        if pelib.is_palindrome(str(i)):
            if pelib.is_palindrome(Denary2Binary(i)):
                total += i
    return total

def Denary2Binary(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n < 0:  raise ValueError, "must be a positive integer"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr


#print Denary2Binary(585)
print p36()
