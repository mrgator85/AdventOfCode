
def applyMask(mask, value):
    valueString = "{0:0>36b}".format(int(value))
    v = list(valueString)
    for i in range(len(valueString)):
        if(mask[i] != 'X'):
            v[i] = mask[i]
    return int("".join(v), 2)
def applyAddressMask(mask, address):
    valueString = "{0:0>36b}".format(int(address))
    v = list(valueString)
    for i in range(len(valueString)):
        if(mask[i] == '1'):
            v[i] = '1'
        elif(mask[i] == 'X'):
            v[i] = 'X'
    return "".join(v)
def getAddresses(address):
    ret = []
    a = list(address)
    idx = [x for x in range(len(a)) if a[x] == 'X']
    xs = ["{0:b}".format(x).zfill(len(idx)) for x in range(pow(2, len(idx)))]
    for x in xs:
        for i in range(len(x)):
            a[idx[i]] = x[i]
        ret.append(int("".join(a), 2))
    return ret       

def executeProgram(program):
    memory = {}
    mask = ''
    for com in program:
        c, p = getCommand(com)
        if(c[0] == 'mem'):
            memory[c[1]] = applyMask(mask, p)
        else:
            mask = p
    return sumNonZero(memory)
def executeProgram2(program):
    memory = {}
    mask = ''
    for com in program:
        c, p = getCommand(com)
        if(c[0] == 'mem'):
            addresses = getAddresses(applyAddressMask(mask, c[1]))
            for a in addresses:
                memory[a] = int(p)
        else:
            mask = p
    return sumNonZero(memory)
def getCommand(l):
    '''Extract the command and parameter from the line
       command will be in a tuple to hold address if present'''
    c,p = l.split('=')
    if(c.strip() == 'mask'):
        return (c.strip(),), p.strip()
    else:
        m, a = c.split('[')
        return (m.strip(), int(a.strip()[:-1])), p.strip()

def sumNonZero(m):
    return sum([m[x] for x in m.keys() if m[x] != 0])

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        prog = f.readlines()
        print(executeProgram2(prog))    
    