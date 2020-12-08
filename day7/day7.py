
import re
class Bag(object):
    '''Class to describe a Bag object, made up of name 
       and a contents.  Contents is a list of tuples containing 
       a Bag and a quantity'''
    def __init__(self, description, contents):
        self.description = description
        self.contents = contents
        self.gold = self.containsGold()
    def containsGold(self, n = 1):
        #print(self.contents)
        return 'shiny gold' in [x[0] for x in self.contents] 

class Counter(object):
    def __init__(self, initValue=0):
        self.v = initValue; 
    def inc(self, val=1):
        self.v = self.v + 1       
def parseRule(line):
    nameString, ruleString = line.split('contain')
    name = nameString.split('bag').pop(0).strip()
    rules = ruleString.split(',')
    contents = []
    for r in rules:
        v = re.search(r'[0-9]+', r)
        if(v):
            num = int(v.group(0))
            desc = re.split(r'[0-9]+?|bag', r.strip())[1]
            contents.append((desc.strip(), int(num)))
        
    #print(contents)
    return Bag(name, contents)

def buildGraph(lines):
    bags = {}
    for l in lines:
        print(l)
        bag = parseRule(l)
        bags[bag.description] = bag
    return bags

def findGold(g, visited, node, counter):
    if(node not in visited):
        if(g[node].containsGold()):
            print('found gold')
            counter.inc()
        visited.append(node)
        for c in g[node].contents:
            findGold(g, visited, c[0], counter)

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        g = buildGraph(f.readlines())
        print(g.keys())
        bagCount = 0
        for k in g.keys():
            visited = []
            counter = Counter(0)
            findGold(g, visited, k, counter)
            #print(counter)
            if(counter.v > 0):
                bagCount = bagCount + 1
        print(bagCount)