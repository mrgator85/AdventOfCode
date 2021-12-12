# The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

# Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?



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

with open("input.txt", "r") as f:
    ret = 0
    world = []
    risks = []
    risk_coords = []
    for l in f.readlines():
        print(l)
        world.append([int(v) for v in l.strip()])
    print(world[1][2])
    maxy = len(world)-1
    maxx = len(world[0])-1
    print(len(world))
    print(len(world[0]))
    for y in range(len(world)):
        for x in range(len(world[y])):
            
            v = world[y][x]
            #print("Checking {} {}: {}".format(x,y,v))
            xs = list(range(getless(x), getmax(x,maxx)+1, 1))
            ys = list(range(getless(y), getmax(y,maxy)+1,1))
            vals = []
            if(x-1 >= 0):
                print("{},{}: {}".format(y, getless(x), world[y][getless(x)]))
                vals.append(world[y][getless(x)])
            if(x+1 <= maxx):
                print("{},{}: {}".format(y, getmax(x, maxx), world[y][getmax(x, maxx)]))
                vals.append(world[y][getmax(x, maxx)])
            if(y-1 >=0):
                print("{},{}: {}".format(getless(y), x, world[getless(y)][x]))
                vals.append(world[getless(y)][x])
            if(y+1 <=maxy):
                print("{},{}: {}".format(getmax(y,maxy), x, world[getmax(y,maxy)][x]))
                vals.append(world[getmax(y,maxy)][x])

            # for iy in ys:
            #     #print("    {},{} <= {}".format(x,iy,world[iy][x]))
            #     if(world[iy][x] < v):
            #         lowest = False
            # for ix in xs:
            #     #print("    {},{} <= {}".format(ix,y,world[y][ix]))
            #     if(world[y][ix] < v):
            #         lowest = False

            if all(v < x for x in vals):
                #print("{},{} - {}".format(x,y,v))
                print("Lowest --- v: {} - vals: {}".format(v, vals))
                risk_coords.append((v, y, x))
                risks.append(v+1)
                ret = ret + v + 1
            else:
                print("Not Lowest --- v: {} - vals: {}".format(v, vals))

    print(risk_coords)
    print(sum(risks))
    print(ret)

            
 


    