def findNthSpoken(spoken, n):
    turn = 0
    lastindx = {}
    lastnumber = 0

    while(turn < n):
        if(turn < len(spoken)):
            v = lastnumber
            #lastindx[spoken[turn]] = turn 
            lastnumber = spoken[turn]
            lastindx[v] = turn - 1
            #print(turn+1)
            #print(lastnumber)
            #print('----')
        else:
            v = lastnumber
            if(lastnumber in lastindx.keys()):
                #print(f"----{turn} --- {lastindx[lastnumber]}")
                lastnumber = turn - 1 - lastindx[lastnumber]
                lastindx[v] = turn -1 
            else:
                lastnumber = 0
                lastindx[v] = turn - 1
            #print(turn+1)
            #print(lastnumber)
            #print('----')
        
        turn = turn + 1
    return lastnumber

def findLastIndexOf(a, v):
    return len(a) - 1 - a[::-1].index(v)


if __name__ == "__main__":
    sample_input = [0, 3, 6]
    my_input = [8, 0, 17, 4, 1, 12]
    print(findNthSpoken(my_input, 30000000))
