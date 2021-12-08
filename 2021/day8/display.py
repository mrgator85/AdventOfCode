

with open("input.txt", "r") as f:
    inputs = []
    outputs = []
    for l in f.readlines():
        i, j = l.split('|')
        inputs.append(j.strip())
        outputs.append(i.strip())
    count = 0
    for r in inputs:
        for s in r.split(): 
            if len(s.strip()) in [2, 7, 3,4]:
                count = count + 1
    print(count)