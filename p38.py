#p38

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

def p38(n):
	maxpd = 0
	pd = ''
	for i in range(1,n):
		for j in range(2,10): #2 to 9
			pd = ''
			for k in range(1,j+1):
				pd = pd + str(i*k)
			#print pd,
			if ispandigital(pd):
				if int(pd) > maxpd:
					maxpd = int(pd)
					print "new max pd!", maxpd
			#print
	return maxpd

print p38(100000)



