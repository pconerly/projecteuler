#p28.py
def p28(n): #n should be odd
	n -= 1
	total = 1
	count = 1
	for i in range(1,n/2+1,1):
		for j in range(4): #patrick did the same thing, kinda
			count += i*2
			total += count 
			#print count, total
	return total

print p28(1001)
