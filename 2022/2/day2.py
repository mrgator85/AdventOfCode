def get_outcome(opp, mine):
    c = {'X': 'A', 'Y':'B', 'Z':'C'}
    if(opp == c[mine]):
        return 3
    if(opp == 'A' and c[mine] == 'B'):
        return 6
    if(opp == 'B' and c[mine] == 'C'):
        return 6
    if(opp == 'C' and c[mine] == 'A'):
        return 6
    else:
        return 0
def get_play(opp, outcome):
    ptmap = {'X':1, 'Y':2, 'Z':3, 'A':1, 'B':2, 'C':3}
    if(outcome == 'Y'): #draw
        return ptmap[opp]
    if(outcome == 'X' and opp == 'A'):
        return ptmap['C']
    if(outcome == 'X' and opp == 'B'):
        return ptmap['A']
    if(outcome == 'X' and opp == 'C'):
        return ptmap['B']
    if(outcome == 'Z' and opp == 'A'):
        return ptmap['B']
    if(outcome == 'Z' and opp == 'B'):
        return ptmap['C']
    if(outcome == 'Z' and opp == 'C'):
        return ptmap['A']
with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    total = 0
    total2 = 0
    ptmap = {'X':1, 'Y':2, 'Z':3}
    omap = {'X':0,'Y':3,'Z':6}
    for l in lines:
        o, m = l.split()
        total = total + ptmap[m] + get_outcome(o, m)
        total2 = total2 + omap[m] + get_play(o,m)
    print(total)
    print(total2)

