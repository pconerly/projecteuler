def invsqrsum(invsqr):
	sum = 0.0
	for j in range(len(invsqr)):
		sum += 1.0/float((invsqr[j]**2))
	return sum

def identities_setup(end = 45, deep = 2, depth = 0, nums = [], identities = []):
    end += 1
    for i in range(2, end):
        nums.append(i)
        for j in range(i, end):
            nums.append(j)
            identities = identities + identities_recur(end, deep, depth + 2, nums)
            nums.pop(-1)
        nums.pop(-1)
    identities = removedups(identities)
    return identities

def removedups(identities):
    identities.sort()
    nodupes = []
    nodupes.append(identities[0])
    for i in range(len(identities)):
        if nodupes[-1] != identities[i]:
            nodupes.append(identities[i])
    return nodupes

def identities_recur(end = 45, deep = 2, depth = 1, nums = [], identities = []):
    if depth == deep:
        return []
    if invsqrsum(nums) == 0.5:
        identities.append([0.5] + nums)
    for z in range(2,end):
        if invsqrsum(nums) == 1.0/(z**2):
            identities.append([z, 'produced by'] + nums)
    for i in range(nums[-1],end):
        nums.append(i)
        identities = identities + identities_recur(end, deep, depth + 1, nums)
        nums.pop(-1)
    return identities

identities = identities_setup(45, 4)
for i in range(len(identities)):
    print identities[i]

def pairs152(n):
    n = n+1
    print
    print "pair identities"
    for i in range(2,n):
        for j in range(i,n):
            if (1.0/(i**2) + 1.0/(j**2)) == 1.0/2:
                print i, j, 'produce 1/2 !!!'
            for k in range(2,81):
                if (1.0/(i**2) + 1.0/(j**2)) == 1.0/(k**2):
                    print i, j, 'produce', k
                    #print 1.0/(i**2), 1.0/(j**2), 'produce', 1.0/(k**2)

#pairs152(45)

def triplets152(n):
    n = n+1
    print
    print "triplet identities"
    for i in range(2,n):
        for j in range(i,n):
            for k in range(j,n):
                if (1.0/(i**2) + 1.0/(j**2) + 1.0/(k**2)) == 1.0/2:
                    print i, j, k, 'produce 1/2 !!!'
                for z in range(2,81):
                    if (1.0/(i**2) + 1.0/(j**2) + 1.0/(k**2)) == 1.0/(z**2):
                        print i, j, k, 'produce', z
                        #print 1.0/(i**2), 1.0/(j**2), 1.0/(k**2), 'produce', 1.0/(m**2)

#triplets152(45)

def quartets152(n):
    n = n+1
    print
    print "quartets identities"
    for i in range(2,n):
        for j in range(i,n):
            for k in range(j,n):
                for m in range(k, n):
                    if (1.0/(i**2) + 1.0/(j**2) + 1.0/(k**2) + 1.0/(m**2)) == 1.0/2:
                         print i, j, k, m, 'produce 1/2 !!!'
                for z in range(2,81):
                    if i == j == k == m:
                        pass
                    elif (1.0/(i**2) + 1.0/(j**2) + 1.0/(k**2) + 1.0/(m**2)) == 1.0/(z**2):
                        print i, j, k, m, 'produce', z
                    #print 1.0/(i**2), 1.0/(j**2), 1.0/(k**2), 'produce', 1.0/(m**2)

#quartets152(45)

def quintets152(n):
    n = n+1
    print
    print "quintets identities"
    for i in range(2,n):
        for j in range(i,n):
            for k in range(j,n):
                for m in range(k, n):
                    for o in range(m, n):
                        if (1.0/(i**2) + 1.0/(j**2) + 1.0/(k**2) + 1.0/(m**2) + 1.0/(o**2)) == 1.0/2:
                            print i, j, k, m, o, 'produce 1/2 !!!'
                        for z in range(2,81):
                            if i == j == k == m == 0:
                                pass
                            elif (1.0/(i**2) + 1.0/(j**2) + 1.0/(k**2) + 1.0/(m**2) + 1.0/(o**2)) == 1.0/(z**2):
                                print i, j, k, m, o, 'produce', z
                            #print 1.0/(i**2), 1.0/(j**2), 1.0/(k**2), 'produce', 1.0/(m**2)

#quintets152(45)
