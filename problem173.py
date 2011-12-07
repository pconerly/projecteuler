#p173

def problem173(n): #n is number of tiles max
	#find number of lamina squares
	i = 1
	laminacount = 0
	while (i+2)**2 - i**2 <= n:
		j = 2
		while (i+j)**2 - i**2 <= n:
			laminacount += 1
			#print laminacount, j, i
			j += 2
		i +=1
	return laminacount

print problem173(1000000)
