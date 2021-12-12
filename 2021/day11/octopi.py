
sample = ['5483143223',
            '2745854711',
            '5264556173',
            '6141336146',
            '6357385478',
            '4167524645',
            '2176841721',
            '6882881134',
            '4846848554',
            '5283751526']
realinput = ['4438624262',
'6263251864',
'2618812434',
'2134264565',
'1815131247',
'2612457325',
'8585767584',
'7217134556',
'2825456563',
'8248473584']

def allZero(i, d):
    for y in range(len(i)):
        for x in range(len(i[y])):
            if(i[y][x] !=0):
                return False
    print("-------------Day {}".format(d))
def getless(v):
    if v == 0:
        return 0
    else:
        return v-1

def getmax(v, m):
    if v == m:
        return m
    else:
        return v+1
def getFlashes(i):
    res = []
    for y in range(len(i)):
        for x in range(len(i[y])):
            if(i[y][x] > 9):
               res.append((y,x))
    return res

def processDay(i, d):
    for y in range(len(i)):
        for x in range(len(i[y])):
            i[y][x] = i[y][x] + 1
    maxy = len(i)-1
    maxx = len(i[0])-1
    flashes = getFlashes(i)
    flashed = []
    while(len(flashes)>0):
        for f in flashes:
            xs = list(range(getless(f[1]), getmax(f[1],maxx)+1, 1))
            ys = list(range(getless(f[0]), getmax(f[0],maxy)+1,1))
            for yi in ys:
                for xi in xs:
                    if(yi,xi) not in flashed:
                        i[yi][xi] = i[yi][xi] + 1
            i[f[0]][f[1]] = 0
            flashed.append(f)
            flashes = getFlashes(i)
    #allZero(i,d)
    return i, flashed

def printOctopi(i):
    for r in i:
        print(''.join([str(s) for s in r]))


input = []
for l in sample:
    input.append([int(x) for x in l])
flashed = 0
for d in range(1000):
    #print("day {}".format(d+1))
    input, f = processDay(input, d)
    flashed = flashed +len(f) 
    #printOctopi(input)
    if(len(f) == 100):
        print("All Flashed on Day {}".format(d+1))
print(flashed)
            
        

