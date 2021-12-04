def getColumn(m, n):
    return [x[n] for x in m]
def getCommon(m):
    if(m.count('1') > m.count('0')):
        return '1'
    elif(m.count('1') == m.count('0')):
        return '1'
    else:
        return '0'
def getUncommon(m):
    if(m.count('1') < m.count('0')):
        return '1'
    else:
        return '0'

def filter(m, n, i):
    return [x for x in m if x[i] == n]

with open("input.txt", 'r') as f:
    moves = [x.strip() for x in f.readlines()]
    s = ''
    e = ''
    for i in range(len(moves[0])):
        s = s + getCommon(getColumn(moves,i))
        e = e + getUncommon(getColumn(moves,i))
    print(int(s,2)*int(e,2))
    idx = 0
    moves1 = moves.copy()
    moves2 = moves.copy()

    while(len(moves1) > 1):
        moves1 = filter(moves1, getCommon(getColumn(moves1, idx)),idx)
        idx = idx + 1
    idx = 0
    while(len(moves2) > 1):
        moves2 = filter(moves2, getUncommon(getColumn(moves2, idx)),idx)
        idx = idx + 1
    print(int(moves1[0], 2))
    print(int(moves2[0], 2))
    print(int(moves2[0], 2)*int(moves1[0], 2))


    