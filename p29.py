#p29
import time

def p29(n):
	terms = []
	for a in range(2,n+1):
		for b in range(2,n+1):
			terms.append(a**b)
	terms.sort()
	terms = remove_dupes(terms)
	#print terms
	return len(terms)

def remove_dupes(l):
	new = []
	if len(l) == 0:
		return l
	new.append(l[0])
	for i in range(1, len(l)):
		if l[i] != l[i-1]:
			new.append(l[i])
	return new

ptime = 0
ptime -= time.clock()
print p29(100)
ptime += time.clock()
print ptime
