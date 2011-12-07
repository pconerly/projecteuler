#p42
import time

def str_file(loc):
    finput = open(loc, 'r')
    words = []
    for line in finput:
        line.strip()
        line = line.lstrip(r'"')
        line = line.rstrip(r'"\n')
        line = line.split('","')
        words = line
    return words

def p42(loc):
    trinums = []
    total = 0
    for i in range(1,100):
        trinums.append(0.5*i*(i+1))
    words = str_file(loc)
    for w in words:
        wordtotal = 0
        for i in range(len(w)):
            wordtotal += ord(w[i]) - ord('A')+1
        if wordtotal in trinums:
            total += 1
    return total
            

p = 0
p -= time.clock()

loc = "words.txt"

print p42(loc)
p += time.clock()
print p
