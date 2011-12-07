#p30
def p30(n):
	total = 0
	for i in range(10,n):
		#print i,
		expsum = 0
		for j in range(len(str(i))):
			#print int(str(i)[j])**5,
			expsum += int(str(i)[j])**5
		#print i, expsum
		if i == expsum:
			total += expsum
			print i, expsum
		
	return total

print p30(1000000)
