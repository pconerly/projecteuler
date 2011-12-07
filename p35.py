#p35 11/24/2010
def p35(n):
	primes = []
	cirprimes = []
	rottemp = 0
	for i in range(2,n):
		if isprime(i):
			primes.append(i)
	for j in range(len(primes)):
		temp = True
		for k in range(len(str(primes[j]))):
			if k == 0:
				rottemp = rotnum(primes[j])
			else:
				rottemp = rotnum(rottemp)
			if rottemp not in primes:
				temp = False
		if temp == True:
			cirprimes.append(primes[j])
	print cirprimes
	return len(cirprimes)

def rotnum(n):
	#print n,
	n = str(n) + str(n)[0]
	#print n
	rot = ''
	for i in range(len(n)-1):
		rot += n[i+1]
	#print rot
	return int(rot)

def isprime(n):
	'''check if integer n is a prime'''
	if n == 2:
		return True
	elif n % 2 == 0:
		return False
	for x in range(3, int(n**0.5)+2,2):
		if n % x == 0:
			return False
	return True

print p35(1000000)


"""
[2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97,    ----13
113, 131, 311, 
197,  971,719, 
337, 373, 733,
199, 919, 991,  ----12
 1193, 1931, 9311, 3119, 
3779, 7793, 7937,  9377, ----8
11939, 19391, 39119, 91193, 93911,
19937,  37199,  71993,   93719,   99371,  ----10
193939, 199933,319993, 331999,  391939, 393919,  919393,  933199, 939193, 939391,  993319, 999331] ---12

13+12+8+10+12 = 55!

101, 103, 107, 
701, 709, 
1013, 1031, 1097, 1103,  907, 1301, 
3001, 3011, 3037, 
7001, 7019, 7109,  9007, 9091, 10007, 10099, 10103, 10193, 10301, 10909,30011, 30119, 31019, 13001,70001, 70003, 70009, 70019, 70793, 70937,77093, 90007, 90019, 90071, 91009,97001,990001,100003, 100103, 100193, 100931, 101939, 103001, 109391, 109937, 110939, 300007, 300073, 300119, 300779, 307079, 310019, 700001, 700109, 700303, 700937, 900007, 900019, 900091, 900701, 901009, 901193, 909371,930011, 930077, 930707,939011, 390119,307,

"""
