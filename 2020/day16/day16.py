def parseFile(f):
    fields = {}
    myTicket = []
    nearby = []
    ## This is lazy
    with open(f, 'r') as fi:
        lines = fi.readlines()
        #find end of rules
        ir = lines.index('your ticket:\n')
        im = ir + 1 #line iwth my ticket
        it = ir + 4 #first line with other tickets
        for l in lines[:ir-1]:
            n, r = l.strip().split(': ')
            print(f"field: {n}, rule: {r}")
            fields[n] = r
        myTicket = [int(n) for n in lines[im].strip().split(',')]
        for l in lines[it:]:
            nearby.append([int(n) for n in l.strip().split(',')])
        return fields, myTicket, nearby

def parseRule(s):
    ranges = s.strip().split(' or ')
    sets = []
    for r in ranges:
        min, max = r.split('-')
        sets.append(set(range(int(min), int(max)+1)))
    return set.union(*sets)


if __name__ == "__main__":
  fields, my, nearby = parseFile('input.txt')
  #convert field rules into sets
  allnums = set()
  invalid = []
  ##part 1
  for f in fields.keys():
      fields[f] = parseRule(fields[f])
      allnums = allnums.union(fields[f])
  for n in nearby:
      invalid.extend(set(n).difference(allnums))
  print(sum(invalid))
  # part 2
  print(len(nearby))
  valid = [n for n in nearby if set(n).issubset(allnums)]
  print(len(valid))
  columns = []
  ks = {}
  while(fields.keys()):
    for i in range(len(nearby[0])):
        ks[i] = []
        c = [x[i] for x in valid]
        for k in fields.keys():
            validrules = [x for x in c if x in fields[k]]
            if(len(validrules) == len(c)):
                ks[i].append(k)
    for d in ks.keys():
        if(len(ks[d]) == 1):
            print(f"--->{d}: {ks[d]}")
            fields.pop(ks[d][0])
            break
    
    #look at std out, manually decode your ticket, because I am lazy
  

