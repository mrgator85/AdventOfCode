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
class Waypoint(object):
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty
    def moveNorth(self, v):
        self.y = self.y + v
    
    def moveSouth(self, v):
        self.y = self.y - v
    def moveEast(self, v):
        self.x = self.x + v
    def moveWest(self, v):
        self.x = self.x - v
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
        if(op == 'R'):
            self.rotateRight(v)
        if(op == 'L'):
            self.rotateLeft(v)
    def rotateRight(self, d):
        ix = self.x
        iy = self.y
        if(d == 90):
            self.x = iy
            self.y = ix * -1
        if(d == 180):
            self.x = ix * -1
            self.y = iy * -1
        if(d == 270):
            self.x = iy * -1
            self.y = ix
    def rotateLeft(self, d):
        ix = self.x
        iy = self.y
        if(d == 90):
            self.x = iy * -1
            self.y = ix 
        if(d == 180):
            self.x = ix * -1
            self.y = iy * -1
        if(d == 270):
            self.x = iy 
            self.y = ix * -1

class WaypointShip(object):
    def __init__(self, startx, starty, wx, wy):
        self.x = startx
        self.y = starty
        self.waypoint = Waypoint(wx, wy)
    def jump(self, t):
        self.x = self.x + (self.waypoint.x * t)
        self.y = self.y + (self.waypoint.y * t)
    def move(self, m):
        op = m[0]
        v = int(m.strip()[1:])
        if(op == 'F'):
            self.jump(v)
        else:
            self.waypoint.move(m)
        #print(f"x:{self.x} y:{self.y} waypoint:{self.waypoint.x}, {self.waypoint.y}")
if __name__ == "__main__":
    ship = Ship(0,0)
    wship = WaypointShip(0,0, 10, 1)
    with open('input.txt', 'r') as f:
        for l in f:
            ship.move(l.strip())
            wship.move(l.strip())
    print(abs(ship.x) + abs(ship.y))
    print(abs(wship.x) + abs(wship.y))