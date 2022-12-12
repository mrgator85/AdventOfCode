from anytree import Node, NodeMixin,RenderTree, search


class Element (NodeMixin):
    def __init__(self, name, dir=False,size=0, parent=None, children=None):
        self.size = size
        self.name = name
        self.parent=parent
        self.dir = dir
        if children:
            self.children = children
    def calculate_size(self):
        if(self.size == 0):
            return sum([e.calculate_size() for e in self.children])
        else:
            return self.size

def printTree(tree):
    for pre, fill, node in RenderTree(root):
        print("%s%s %s" % (pre, node.name, node.size))

nodes = []

root = Element("root")
currentNode = root
nodes.append(root)
with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    for l in lines:
        #print("line: %s" % l)
        if(l == '$ cd /'):
            #print("cd to root")
            currentNode = root
            #print(currentNode)
        elif(l == '$ cd ..'):
            print("CURRENTDIR: %s" % currentNode.name)
            currentNode = currentNode.parent
        elif(list(l)[0] != '$'):
            #print("ls dir: %s" % l)
            s, n = l.split(' ')
            if(s == 'dir'):
                if(len(list(filter(lambda node: node.name == n and node.dir, currentNode.children))) < 1):
                    print("adding dir %s" % n)
                    nodes.append(Element(n, True, parent=currentNode))
            else:
                if(len(list(filter(lambda node: node.name == n and node.dir, currentNode.children))) < 1):
                    nodes.append(Element(n, False, int(s), parent=currentNode))
        elif('$ cd ' in l): #change directory
            #print("change dir %s" % l)
            n = l.split()[-1]
            #print("changing to %s" % n)
            #printTree(root)
            #print([x.name for x in currentNode.children])
            currentNode = list(filter(lambda node: node.name == n and node.dir, currentNode.children))[0]
            #print(results)
            #currentNode = search.find(currentNode, filter_=lambda node: node.name==n and node.dir, maxlevel=1)
            if(not currentNode):
                print("NODE NOT FOUND: %s" % l)
    for n in nodes:
        n.size = n.calculate_size()
    count = 0
    for n in nodes:
        if n.dir and n.size <100001:
            count = count + n.size
    
    freespace = 70000000 - root.size
    print(freespace)
    needed = 30000000 - freespace
    print(needed)
    res = search.findall(root, filter_=lambda node: node.size >= needed and node.dir)
    for r in res:
        print(r.name, r.size)
    sizes = [r.size for r in res]
    sizes.sort()
    print(sizes[0])
    #printTree(root)
    print(count)
