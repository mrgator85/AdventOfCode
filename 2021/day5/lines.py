class Grid(object):

    def __init__(self,x,y):
        self.array = []
        for i in range(x):
            row = []
            for j in range(y):
                row.append(0)
            self.array.append(row)
    def range2(self,x1, x2):
        s = [x1, x2]
        s.sort()
        vals = list(range(abs(s[1]-s[0]+1)))
        if(x1 > x2):
            vals = [-1*v for v in vals]

        #print("{0},{1} => {2}".format(x1, x2, vals))
        return vals
    
    def countGreaterThan(self, v):
        count = 0
        for r in self.array:
            for x in r:
                if(x > v):
                    count = count + 1
        return count

        
    def drawLine(self,s):
        string1, string2 = s.split('->')
        x1s, y1s = string1.split(',')
        x2s, y2s = string2.split(',')
        x1 = int(x1s.strip())
        y1 = int(y1s.strip())
        x2 = int(x2s.strip())
        y2 = int(y2s.strip())
        print("{0},{1} -> {2},{3}".format(x1, y1, x2,y2))
        
        if(x1==x2):
           for j in self.range2(y1,y2):
               self.array[x1][y1+j] = self.array[x1][y1+j] + 1
        elif(y1 == y2):
           for i in self.range2(x1,x2):
               self.array[x1+i][y1] = self.array[x1+i][y1] + 1
        else:
            xvals = self.range2(x1, x2)
            print(xvals)
            yvals = self.range2(y1, y2)
            print(yvals)
            for i in range(len(xvals)):
                self.array[x1+xvals[i]][y1+yvals[i]] = self.array[x1+xvals[i]][y1+yvals[i]] + 1
    def printGrid(self):
        for r in self.array:
            print(r)

with open("input.txt") as f:
    grid = Grid(1000, 1000)
    for l in f.readlines():
        grid.drawLine(l.strip())
    
    grid.printGrid()

    print(grid.countGreaterThan(1))