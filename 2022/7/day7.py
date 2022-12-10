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
            currentNode = currentNode.parent
        elif(list(l)[0] != '$'):
            #print("ls dir: %s" % l)
            s, n = l.split(' ')
            if(s == 'dir'):
                print("adding dir %s" % n)
                if(not search.find_by_attr(root, n, name='name')):
                    nodes.append(Element(n, True, parent=currentNode))
            else:
                if(not search.find_by_attr(root, n, name='name')):
                    nodes.append(Element(n, False, int(s), parent=currentNode))
        elif('$ cd ' in l): #change directory
            print("change dir %s" % l)
            n = l.split()[-1]
            print("changing to %s" % n)
            currentNode = search.find_by_attr(root, n, name='name')
            print(currentNode)
    for n in nodes:
        n.size = n.calculate_size()
    count = 0
    for n in nodes:
        if n.children and n.size <100001:
            count = count + 1
    
    printTree(root)
    print(count)
