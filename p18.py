#problem 18 11/24/2010
def p18():
    finput = open("problem18.txt", 'r')
    nums = []
    print finput
    for line in finput:
        line.strip()
        line = line.rstrip(r'\n')
        line = line.split()
        nums.append(line)
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            nums[i][j] = int(nums[i][j])
    print nums

    h = len(nums)-1
    for i in range(1,len(nums)): #0 to height
        for j in range(len(nums[h-i])):
            print h, i, j
            nums[h-i][j] += max(nums[h-i+1][j],nums[h-i+1][j+1])

    return nums[0][0]

print p18()
