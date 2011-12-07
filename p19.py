def p19():
	day = 1 #first day of 1901 is a tuesday
	months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	leapyears = []
	count = 0
	for i in range(1900,1999):
		if i % 4 == 0:
			leapyears.append(i)
	
	for i in range(1901,2001): # years
		for j in range(12): #months
			for k in range(months[j]):
				if k == 0 and day == 6:
					count += 1
				day = add_day(day)
				if j == 1 and k == 28 and i in leapyears:  #leap days
					day = add_day(day)
	return count



def add_day(n):
	if n == 6:
		n = 0
		return n
	else:
		return n+1

print p19()
