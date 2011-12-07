#p32
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

def remove_dupes(l):
	
	if len(l) == 0:
		return None
	new = []
	new.append(l[0])
	for i in range(1,len(l)):
		if l[i] != l[i-1]:
			new.append(l[i])
	return new

def p32():
	pds = [] #pandigitals
	for i in range(1,9999):
		for j in range(1,999):
			if ispandigital(str(i)+str(j)+str(i*j)):
				print i, j, i*j
				pds.append(i*j)
	pds.sort()
	print "before", pds
	pds = remove_dupes(pds)
	print "after", pds
	return sum(pds)

print p32()
	

