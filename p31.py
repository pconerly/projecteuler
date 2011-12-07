#p31
def p31():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    depth = 0
    cur = 0
    count = 0
    for i in range(int((200-cur)/coins[depth])+1): #200
        cur += i*coins[depth]
        print " " * depth, "i", i, "cur", cur
        depth += 1
        for j in range(int( (200-cur) /coins[depth])+1): #100
            
            cur += j*coins[depth]
            print " " * depth, "j", j, "cur", cur
            depth += 1
            for k in range(int( ((200-cur) /coins[depth]) )+1 ): #50
                
                cur += k*coins[depth]
                print " " * depth, "k", k, "cur", cur
                depth += 1
                for l in range(int( (200-cur) /coins[depth])+1): #20
                    
                    
                    cur += l*coins[depth]
                    print " " * depth, "l", l, "cur", cur
                    depth += 1
                    for m in range(int( (200-cur) /coins[depth])+1): #10
                        #print m,
                        
                        cur += m*coins[depth]
                        depth += 1
                        for n in range(int( (200-cur) /coins[depth])+1): #5
                            #print n,
                            cur += n*coins[depth]
                            depth += 1
                            for o in range(int( (200-cur) /coins[depth])+1): #2
                                #print o
                                count += 1
                            depth -= 1
                            cur -= n*coins[depth]
                        depth -= 1
                        cur -= m*coins[depth]
                        
                    
                    depth -= 1
                    cur -= l*coins[depth]
                
                depth -= 1
                cur -= k*coins[depth]
            
            depth -= 1
            cur -= j*coins[depth]
        
        depth -= 1
        cur -= i*coins[depth]

    return count

print p31()
