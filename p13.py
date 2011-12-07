#p13

def p13():
    finput = open("problem13.txt", 'r')
    nums = []
    #print finput
    for line in finput:
        line = line.rstrip(r'\n')
        nums.append(int(line))

    total = 0
    for i in range(len(nums)):
        total += nums[i]

    return str(total)[0:10]

print p13()
