def get_set(a):
    min, max = a.split('-')
    return set(range(int(min), int(max)+1))

with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    count = 0
    count2 = 0
    for l in lines:
        a, b = l.split(',')
        sa = get_set(a)
        sb = get_set(b)
        print(sa, sb)
        if(sa.issubset(sb) or sa.issuperset(sb)):
            count = count + 1
        if(not sa.isdisjoint(sb)):
            count2 = count2 + 1
        
    print(count)
    print(count2)
