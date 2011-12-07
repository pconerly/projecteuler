#p22
def p22_bad():
    finput = open("problem22.txt", 'r')
    names = []
    alphascore = dict()
    alphascore = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
                  'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19,
                  'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    for line in finput:
        line.strip()
        line = line.rstrip(r'\n')
        line = line.split('","')
        
        names = line
    print type(line)
    print type(names)
    print type(names[0])
    print type(names[0][0])
    print names[0]
    names.sort()
    tns = 1 #total name scores
    for i in range(len(names)):
        ns = 0
        #print type(names[0])
        #print names[0][0]
        for j in range(len(names[i])):
            pass
            #print i, j
            #print names[i][j]
            #ns += alphascore[names[i][j]]
        #tns *= ns*i
    return tns

def p22():
    finput = open("problem22.txt", 'r')
    names = []
    alphascore = dict()
    alphascore = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
                  'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19,
                  'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    for line in finput:
        line.strip()
        line = line.lstrip(r'"')
        line = line.rstrip(r'"\n')
        line = line.split('","')
        names = line
    names.sort()
    tns = 0 #total name scores
    for i in range(len(names)):
        ns = 0
        for j in range(len(names[i])):
            #print j, names[i][j], alphascore[names[i][j]]
            ns += alphascore[names[i][j]]
        tns += ns*(i+1)
    return tns

print p22()
