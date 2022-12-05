class Storage(object):
    def __init__(self):
        self.stacks = []
        # self.stacks.append(['Z','N'])
        # self.stacks.append(['M','C','D'])
        # self.stacks.append(['P'])
        self.stacks.append(list('HBVWNMLP'))
        self.stacks.append(list('MOH'))
        self.stacks.append(list('NDBGFQML'))
        self.stacks.append(list('ZTFQMWG'))
        self.stacks.append(list('MTHP'))
        self.stacks.append(list('CBMJDHGT'))
        self.stacks.append(list('MNBFVR'))
        self.stacks.append(list('PLHMRGS'))
        self.stacks.append(list('PDBCN'))
    def move(self, s, d, q):
        for i in range(q):
            v = self.stacks[s-1].pop()
            self.stacks[d-1].append(v)
    def print(self):
        for i in range(9):
            print(self.stacks[i]) 
    def movemany(self, s, d, q):
        i = q*-1
        data = self.stacks[s-1][i:]
        self.stacks[s-1] = self.stacks[s-1][:len(self.stacks[s-1])-q]
        self.stacks[d-1].extend(data)

if __name__ == "__main__":
    s = Storage()
    with open('input.txt', 'r') as f:
        lines = [x.strip() for x in f.readlines()]
        for l in lines:
            x, q, y, t, z, d = l.split()
            s.movemany(int(t), int(d), int(q))
        s.print()
