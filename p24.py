import math
#for math.factorial!

#p24
def p24():
    digits = 9 #counting from 0
    goal = 1000000 - 1  #APPARENTLY you subtract one.  WTF, euler.
    lexpos = [0]*10
    depth = 0

    print 'dp', 'goal', 'subtr', 'rem'
    
    for depth in range(digits):#probably should be while
        lexpos[depth] = int(goal/math.factorial(digits-depth))
        #print goal, '%',math.factorial(digits-depth), '=', lexpos[depth],'rem', goal % math.factorial(digits-depth)
        for i in range(int(goal/math.factorial(digits-depth))+1):
            print depth, goal,(i)*math.factorial(digits-depth),
            print goal-(i)*math.factorial(digits-depth)
        goal = goal % math.factorial(digits-depth)

    print lexpos
    perm = permutation(lexpos, digits)
    print perm
    #lexpos[
    #perm2 = permutation(lexpos,digits)
    answer = ''
    for i in range(len(perm)):
        answer += str(perm[i])
    return answer

def permutation(lexpos, digits):
    digits += 1
    d = range(digits)
    new = []
    
    for i in range(digits):
        new.append(d[lexpos[i]])
        d.pop(lexpos[i])
    return new

print p24()

def pete():
    #fdsfsd
    #blahanelnfelks:
    pass
