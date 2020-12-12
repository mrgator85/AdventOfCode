class Ship(object):
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty
        self.orientation = 90
        #self.orientations = [0, 90, 180, 270]
    
    def moveNorth(self, v):
        self.y = self.y + v
    
    def moveSouth(self, v):
        self.y = self.y - v
    def moveEast(self, v):
        self.x = self.x + v
    def moveWest(self, v):
        self.x = self.x - v
    def turnLeft(self, d):
        self.orientation = self.orientation - d
        if(self.orientation < 0):
            self.orientation = 360 + self.orientation
        if(self.orientation == 360):
            self.orientation = 0
    def turnRight(self, d):
        self.orientation = self.orientation + d
        if(self.orientation >= 360):
            self.orientation = self.orientation - 360
    def moveForward(self, d):
        if(self.orientation == 0):
            self.moveNorth(d)
        if(self.orientation == 90):
            self.moveEast(d)
        if(self.orientation == 180):
            self.moveSouth(d)
        if(self.orientation == 270):
            self.moveWest(d)
    def move(self, m):
        op = m[0]
        v = int(m.strip()[1:])
        if(op == 'N'):
            self.moveNorth(v)
        if(op == 'S'):
            self.moveSouth(v)
        if(op == 'E'):
            self.moveEast(v)
        if(op == 'W'):
            self.moveWest(v)
        if(op == 'F'):
            self.moveForward(v)
        if(op == 'R'):
            self.turnRight(v)
        if(op == 'L'):
            self.turnLeft(v)

if __name__ == "__main__":
    ship = Ship(0,0)
    with open('input.txt', 'r') as f:
        for l in f:
            ship.move(l.strip())
    print(abs(ship.x) + abs(ship.y))
