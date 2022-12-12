
def isVisible(x,y, g):
    v = g[y][x]
    print(x, y)
    ys = [a[x] for a in g]
    if(v > max(g[y][:x])):
        return True
    if(v > max(g[y][x+1:])):
        return True
    if(v > max(ys[:y])):
        return True
    if(v > max(ys[y+1:])):
        return True
         


with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    d = []
    for l in lines:
        d.append([int(x) for x in list(l)])
    visible = 0
    for y in range (1, len(d)-1):
        for x in range(1, len(d[0])-1):
            if(isVisible(x, y, d)):
                visible = visible + 1
    print(visible + len(d) + len(d) + len(d[0]) + len(d[0]) -4)