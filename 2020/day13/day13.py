import math

def findNearestDepart(seconds, buses):
    delay = 10000000000
    closest = 0
    for b in buses:
        t = 0
        p = 1
        while t < seconds:
            t = b*p
            p = p + 1
        d = t-seconds
        print(f"b: {b}, d: {d}")
        if(d < delay):
            delay = d
            closest = b 
    return closest, delay
    
def findearliestSchedule(offsets, inservice):
    t = q = 1
    i = 1
    c = 1
    memo = {}
    while(i < len(offsets)+1):
        r = True
        for b in offsets[0:i]:
            v = t+b[1]
            n = b[0]
            r = r and isMultiple2(v, n)
        if(not r):
            t = t + c
        else:
            c = math.prod([b[0] for b in offsets[0:i]])
            i = i + 1
    return t
def isMultiple(v, n):
    x = n
    i = 1
    while(x < v):
        x = n * i
        i = i + 1
    if(x == v):
        return True
    else:
        return False
def isMultiple2(v, n):
    return v % n == 0

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        t = int(f.readline().strip())
        schedule = f.readline().strip().split(',')
        inservice = [int(x) for x in schedule if x != 'x']
        offsets = []
        offset = 0
        for x in schedule:
            if(x != 'x'):
                offsets.append((int(x), offset))
            offset = offset + 1
        
        print(inservice) 

        b, d = findNearestDepart(t, inservice) 
        print(b *d)
        print(findearliestSchedule(offsets, inservice))