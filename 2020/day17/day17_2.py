import copy
def cycle(m):
    grow(m)
    currentState = copy.deepcopy(m)
    for spot in currentState.keys():
        if(currentState[spot]):
            if(countAdjacent(currentState, spot) not in [2,3]):
                m[spot] = False
        else:
            if(countAdjacent(currentState, spot) == 3):
                m[spot] = True

def countAdjacent(m, spot):
    on = 0
    for w in range(spot[3]-1, spot[3]+2, 1):
        for z in range(spot[2]-1, spot[2]+2, 1):
            for y in range(spot[1]-1, spot[1]+2, 1):
                for x in range(spot[0]-1, spot[0]+2, 1):
                    if((x, y, z,w) in m.keys()):
                        if(m[(x,y,z,w)]):
                            on = on + 1
    if(m[spot]):
        on = on - 1
    #print(f"key:{spot} value:{m[spot]} count: {on}")
    return on

def countOn(m):
    count = 0
    print(len(m.keys()))
    for k in m.keys():
        if m[k]:
            count = count + 1
    return count

def grow(m):
    #grow 
    maxx = max([x[0] for x in m.keys() if x[2] == 0 and x[1] == 0 and x[3] == 0])
    minx = min([x[0] for x in m.keys() if x[2] == 0 and x[1] == 0 and x[3] == 0])
    maxy = max([x[1] for x in m.keys() if x[2] == 0 and x[0] == 0 and x[3] == 0])
    miny = min([x[1] for x in m.keys() if x[2] == 0 and x[0] == 0 and x[3] == 0])
    maxz = max([x[2] for x in m.keys() if x[1] == 0 and x[0] == 0 and x[3] == 0])
    minz = min([x[2] for x in m.keys() if x[1] == 0 and x[0] == 0 and x[3] == 0])
    maxw = max([x[3] for x in m.keys() if x[2] == 0 and x[1] == 0 and x[0] == 0])
    minw = min([x[3] for x in m.keys() if x[2] == 0 and x[1] == 0 and x[0] == 0])
    for w in range(minw-1, maxw+2, 1):
        for z in range(minz-1, maxz+2, 1):
            for y in range(miny-1, maxy+2, 1):
                for x in range(minx-1, maxx+2, 1):
                    if((x, y, z, w) not in m.keys()):
                        m[(x,y,z,w)] = False
def buildMap(s):
    r = s.strip().split('\n')
    midy = int(len(r)/2)
    midx = int(len(r[0])/2)
    xs = list(range(-1*midx, 0, 1)) + list(range(0,midx+1, 1))
    ys = list(range(-1*midy, 0, 1)) + list(range(0,midy+1, 1))
    ret = {}
    for y in range(len(r)):
        print('-----')
        for x in range(len(r[0])):
            print(r[y][x])
            ret[(xs[x], ys[y], 0, 0)] = r[y][x] == '#'
    return ret

def printMap(m, z):
    xs = [x[0] for x in m.keys() if x[2] == z and x[1] == 0] 
    print(xs)
    ys = [x[1] for x in m.keys() if x[2] == z and x[0] == 0]
    print(ys)
    for y in ys:
        r = []
        for x in xs:
            r.append(m[(x, y, z)])
        print("".join(r))



if __name__ == "__main__":
    input_test = '.#.\n..#\n###'
    input_real = '..#....#\n##.#..##\n.###....\n#....#.#\n#.######\n##.#....\n#.......\n.#......'
    m = buildMap(input_real)
    #printMap(m,0)
    for i in range(6):
        print(i)
        cycle(m)
    print(countOn(m))
    #printMap(0)([x[2