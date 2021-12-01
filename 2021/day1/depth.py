
def count_increase(lines):
    increasing = 0
    val = lines[0]
    for l in lines[1:]:
        if(l > val):
            increasing = increasing + 1
        val = l
    return increasing

with open("input.txt", 'r') as f:
    lines = [int(x.strip()) for x in f.readlines()]
    print(count_increase(lines))
    ar = []
    for a in range(len(lines)):
        ar.append(sum(lines[a:a+3]))
    print(count_increase(ar))
