#p17
def p17():
    teens = dict()
    teens = {'10':3, '11':6, '12':6, '13':8, '14':8, '15':7, '16':7, '17':9, '18':8, '19':8}
    ones = dict()
    ones = {'0':0, '1':3, '2':3, '3':5, '4':4, '5':4, '6':3, '7':5, '8':5, '9':4}
    tens = dict()
    tens = {'2':6, '3':6, '4':5, '5':5, '6':5, '7':7, '8':6, '9':6}

    total = 0
    for i in range(1,1001):
        temp = str(i)
        print temp,
        l = 0
        if int(temp) == 1000: #thousand
            """
            l += ones[temp[0:1]]
            l += 8 #thousand
            if temp[1:2] != 0:
                l += 3
                temp = temp[1:]
            elif temp[2:3] != 0:
                l += 3
                temp = temp[2:]
            elif temp[3:4] != 0:
                l += 3
                temp = temp[3:]
            else:
                temp = ''
            """
            l = 11
            temp = ''
        if len(temp) == 3: #hundreds
            l += ones[temp[0:1]]
            l += 7 #hundred
            if temp[1] != '0':
                l += 3 #and
                temp = temp[1:]
            elif temp[2] != '0' and temp[1] :#the first one did equal zero, chop off extra,
                l += 3 #and
                temp = temp[2:]            
            elif temp[1:3] == '00':
                temp = ''
        if len(temp) == 2: #tens
            if int(temp) > 19:
                l += tens[temp[0:1]] + ones[temp[1:2]]
            elif int(temp) >= 10:
                l += teens[temp]
                temp = ''
        if len(temp) == 1: #ones
            l += ones[temp]
        total += l
        print l
    return total

print p17()


"""
    one 3
    two 3
    three 5
    four 4
    five 4
    six 3
    seven 5
    eight 5
    nine 4
    """
"""
    eleven
    twelve
    thriteen
    fourteen
    fifteen
    sixteen
    seventeen
    eighteen
    nineteen
    """
"""
    twenty
    thrity
    fourty
    fifty
    sixty
    seventy
    eighty
    ninety
    """
"""
    add 'hundred' = 7
    add 'thousand' = 8
    """
