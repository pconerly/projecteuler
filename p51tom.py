#p51
import pelib
import time

def p51():
	num = 0
	while True:
		num += 1
		if not pelib.isprime(num):
			continue

		for i in range(3):
			strnum = str(num)
			if strnum.count(str(i)) == 0:
				continue
			tally = 1
			for j in range(i+1, 10):
				replaced = int(strnum.replace(str(i), str(j))) 
				if pelib.isprime(replaced):
					tally += 1
			if tally == 8:
				return num


ptime = 0
ptime -= time.clock()
print(p51())
ptime += time.clock()
print(ptime)
