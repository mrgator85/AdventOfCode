
def getGroups(lines):
    groups = []
    group = []
    for l in lines:
        if len(l.strip()) == 0:
            groups.append(group.copy())
            group.clear()
        else:
            group.append(l.strip())
    groups.append(group)
    return groups
def processGroup(g):
    chars = []
    for i in g:
        chars = chars + list(i)
    return len(set(chars))
def processGroup2(g):
    sets = [set(list(x)) for x in g]
    return len(set.intersection(*sets))
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        #print(getGroups(f.readlines()))
        tot = 0
        for g in getGroups(f.readlines()):
            tot = tot + processGroup2(g)
        
        print(f"The Sum is {tot}.")
        