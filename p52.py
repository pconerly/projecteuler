#problem 52
def p52():
    nums = [0]*6
    while True:
        nums[0] += 1
        for i in range(2,7):
            nums[i-1] = nums[0]*i
            base = list(str(nums[0]))
            extension = list(str(nums[i-1]))
            base.sort()
            extension.sort()
            if base == extension:
                if i == 5:
                    print "found it!", nums[0]
                    print "details for nums[0]", base
                    print "details for nums[i]", extension
            else:
                break
            
p52()
