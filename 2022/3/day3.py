def splitString(s):
    s
    s1 = slice(0,len(s)//2)
    s2 = slice(len(s)//2, len(s))
    return s[s1], s[s2]
def getCharVal(c):
    o = ord(c)
    if(o < 91): # uppercase
        return o - 38
    else:
        return o - 96

with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    total = 0
    total2 = 0
    count = 0
    sets = []
    for l in lines:
        c1, c2 = splitString(l)
        sc1 = set(c1)
        sc2 = set(c2)
        #print(sc1, sc2)
        v = sc1.intersection(sc2)
        #print(v)
        #print(getCharVal(list(v)[0]))

        total = total + getCharVal(v.pop())
        

        sets.append(set(l))
        count = count + 1
        if(count == 3):
            count = 0
            v = sets[0].intersection(sets[1]).intersection(sets[2])
            print(v)
            total2=total2 + getCharVal(v.pop())
            sets.clear()
            
    print(total2)
    print(total)
