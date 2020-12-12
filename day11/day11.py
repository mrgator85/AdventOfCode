import copy
def change(b):
    changed = False
    a = copy.deepcopy(b)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(a[i][j] != '.'):
                occupied = countAdjacent(a, i, j)
                if(a[i][j] == 'L' and occupied == 0):
                    b[i][j] = '#'
                    changed = True
                elif(a[i][j] == '#' and occupied > 3):
                    b[i][j] = 'L'
                    changed = True
                else:
                    pass
    return changed

def change2(b):
    changed = False
    a = copy.deepcopy(b)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(a[i][j] != '.'):
                occupied = countOrthogonals(a, i, j) + countDiagonals(a, i, j)
                if(a[i][j] == 'L' and occupied == 0):
                    b[i][j] = '#'
                    changed = True
                elif(a[i][j] == '#' and occupied > 4):
                    b[i][j] = 'L'
                    changed = True
                else:
                    pass
    return changed
def countAdjacent(a, i, j ):
    count = 0
    if(i == 0):
        sx = 0
    else:
        sx = i - 1
    if i+1 == len(a):
        ex = i 
    else:
        ex = i + 1
    if(j == 0):
        sy = 0
    else:
        sy = j - 1
    if(j+1 == len(a[i])):
        ey = j 
    else:
        ey = j + 1
    for x in range(sx,ex+1):
        for y in range(sy, ey+1):
            if(a[x][y] == '#' and not (x == i and y == j)):
                count = count + 1
    return count
def countDiagonals(a, i, j):
    count = 0
    seat = next((a[i+k][j+k] for k in range(1, min([len(a[i:]), len(a[i][j:])]), 1) if a[i+k][j+k] != '.'), '.' )
    if seat == '#':
        count = count + 1
    ##SE 
    seat = next((a[i+k][j-k] for k in range(1, min([len(a[i:]), len(a[i][:j])+1]), 1) if a[i+k][j-k] != '.'), '.')
    if seat == '#':
        count = count + 1
    ##SW
    seat = next((a[i-k][j+k] for k in range(1, min([len(a[:i])+1, len(a[i][j:])]), 1) if a[i-k][j+k] != '.') , '.')
    if '#' == seat:
        count = count + 1
    ##NW
    seat = next((a[i-k][j-k] for k in range(1, min([len(a[:i])+1, len(a[i][:j])+1]), 1) if a[i-k][j-k] != '.'), '.')
    if '#' == seat:
        count = count + 1
    return count
def countOrthogonals(a, i, j):
    count = 0
    ##check EL
    if(i+1 < len(a)):
        for l in a[i+1:]:
            if '#' == l[j]:
                count = count + 1
                break
            elif 'L' == l[j]:
                break
    ##check W
    if(i > 0):
        for l in range(1, len(a[:i])+1, 1):
            if '#' == a[i-l][j]:
                count = count + 1
                break
            elif('L' == a[i-l][j]):
                break
    ##check N
    if(j != 0):
        seat = next((a[i][y] for y in range(j-1, -1, -1) if a[i][y] != '.'), '.')
        if('#' == seat):
            count = count + 1
    ##check S
    if(j+1 < len(a[i])):
        seat = next((a[i][y] for y in range(j+1, len(a[i]), 1) if a[i][y] != '.'), '.')
        if('#' == seat):
            count = count + 1
    return count

def countOccupied(a):
    occ = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(a[i][j] == '#'):
                occ = occ + 1
    return occ
if __name__ == "__main__":
    a = []
    with open('input.txt', 'r') as f:
        for l in f:
            a.append(list(l.strip()))
    count = 0
    changed = True
    c = copy.deepcopy(a)

    while(changed):
        changed = change(a)
        count = count + 1
    print(countOccupied(a))
    print(count)
    print('_*_*_*_*_**_*_*_*_*_**_*_*_')
    changed = True
    while(changed):
        changed = change2(c)
    print(countOccupied(c))

