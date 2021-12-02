def getMove(l):
    [direction, val] = l.split(' ')
    val = int(val)
    if(direction == "forward"):
        return (val, 0)
    elif(direction == "down"):
        return (0, val)
    elif(direction == "up"):
        return (0, -1*val)
    else:
        print("bad direction")
        return (0,0)



with open("input.txt", 'r') as f:
    moves = [getMove(x.strip()) for x in f.readlines()]
    start = (0,0)
    for m in moves:
        start = (start[0] + m[0], start[1] + m[1])
    print(start[0] * start[1])
    # (x, y, aim)
    current = (0, 0, 0)
    for m in moves:
        current = (current[0] + m[0], current[1] + m[0] * current[2], current[2]+m[1])
    print(current[0]*current[1]) 


