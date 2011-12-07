#problem 152

def problem152(cap):
	#finds the number of combinations for inverse squares that sum to 1/2
	half = float(0.5)
	#use recursions
	invsqr = []
	new = 2
	cap += 1
	return p152r(invsqr, new, cap)

def p152r(invsqr, new, cap):
	invsqr.append(new)
	sum = invsqrsum(invsqr)
	#print sum
	success = 0
	for i in range(invsqr[-1]+1,cap):
		if sum + 1/float(i**2) == 0.5:
			success += 1
		elif sum + 1/float(i**2) < 0.5 and sum + invsqrsum(range(i, cap)):
			success += p152r(invsqr, i, cap)
	return success
		
def invsqrsum(invsqr):
	sum = 0
	for j in range(len(invsqr)):
		sum += float((invsqr[j]**2))
		sum = 1/sum
	return sum

def test():
	invsqr = []
	for i in range(3,81):
		invsqr.append(i)
		sum = float(0)
		for j in range(len(invsqr)):
			sum += 1/float((invsqr[j]**2))
		print i, sum

#test()
print problem152(45)
