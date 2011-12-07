#pelib
#This library contains functions that are used
#multiple times in the Project Euler problems
import math

def ispandigital(n):
	n = str(n)
	if len(n) != 9:
		return False
	digits = []
	for i in range(len(n)):
		digits.append(n[i])
	digits.sort()
	#print digits
	for j in range(1,10):
		if j != int(digits[j-1]):
			#print "will return false",
			return False
	return True

#returns true/false depending on primeness
def isprime(p):
    if p == 1:
        return False
    if p == 2:
        return True
    elif p % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(p))+2,2):
        if p % i == 0:
            return False
    return True

def first(word): #for def is_palindrome
    return word[0]

def last(word): #for def is_palindrome
    return word[-1]

def middle(word): #for def is_palindrome
    return word[1:-1]

def is_palindrome(s):
    if first(s) == last(s):
        if len(s) >= 3:
            return is_palindrome(middle(s))
        else:
            return True
    else:
        return False

#sorts list & remove dupes
def remove_dupes(l):
    new = []
    if len(l) == 0:
        return False
    new.append(l[0])
    for i in range(1,len(l)):
        if l[i] != l[i-1]:
            new.append(l[i])
    return new

#import number data file into list.
#numbers may be on multiple lines and seperated by spaces.
def num_file(loc):
    finput = open(loc, 'r')
    nums = []
    for line in finput:
        line.strip()
        line = line.rstrip(r'\n')
        line = line.split()
        nums.append(line)
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            nums[i][j] = int(nums[i][j])
    return nums

#prime factorization
#takes a number and returns a list of the prime factors; with duplicates
#if the number is prime, returns number.
#does not include '1'
def prime_factors(n):
    factors = []
    if n == 1:
        return [1]
    while n % 2 == 0:
        #print n, 2
        n = n / 2
        factors.append(2)
    i = 3
    while i <= math.sqrt(n):
        #print n, i
        if n % i == 0:
            n = n / i
            factors.append(i)
        else:
            i += 1
    if n != 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    print prime_factors(7**2)
    pass








