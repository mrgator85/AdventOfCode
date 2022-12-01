with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    totals = []
    total = 0
    for l in lines:
        if(l == ''):
            totals.append(total)
            total = 0
        else:
            total = total + int(l)
    print(max(totals))
    s = sorted(totals)
    print(s[-3:])
    print(sum(s[-3:]))
