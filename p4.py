def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(s):
    if first(s) == last(s):
        if len(s) >= 3:
            return is_palindrome(middle(s))
        else:
            return True
    else:
        return False

def problem4():
    palis = []
    for i in range(100,999):
        for j in range(100,999):
            if is_palindrome(str(i*j)) == True:
                palis.append((i*j, i, j))
    palis.sort()
    return palis[-1]

print problem4()
