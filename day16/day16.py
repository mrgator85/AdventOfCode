def parseFile(f):
    fields = {}
    myTicket = []
    nearby = []
    ## This is lazy
    with open(f, 'r') as fi:
        lines = fi.readlines()
        print(lines)
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
        print(fields)
        print(myTicket)
        print(nearby)
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
  for f in fields.keys():
      fields[f] = parseRule(fields[f])
      allnums = allnums.union(fields[f])
  print(f"allnums: {allnums}")
  for n in nearby:
      invalid.extend(set(n).difference(allnums))
  print(invalid)    
  print(sum(invalid))
      

