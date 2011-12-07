import math
import time
#p49
def p49():
	for i in range(1000,9999):
		for j in range(1,3334):
			first = i
			second = i+j
			third = i+j*2
			if elements(first) == elements(second) == elements(third):
				if first != second and first != third and second != third:
					if isprime(first) and isprime(second) and isprime(third):
						print str(first)+" " +str(second)+" " +str(third)
	return 'blah'
			
def elements(n):
	new = list(str(n))
	new.sort()
	return new

def isprime(p):
	if p % 2 == 0:
		return False
	for i in range(3,int(math.sqrt(p))+2,2):
		if p % i == 0:
			return False
	return True

ptime = 0
ptime -= time.clock()
print p49()
ptime += time.clock()
print ptime
