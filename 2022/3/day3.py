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
    for l in lines:
        c1, c2 = splitString(l)
        sc1 = set(c1)
        sc2 = set(c2)
        #print(sc1, sc2)
        v = sc1.intersection(sc2)
        #print(v)
        #print(getCharVal(list(v)[0]))

        total = total + getCharVal(v.pop())
    print(total)
