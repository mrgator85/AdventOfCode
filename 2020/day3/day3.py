
def isATree(l, y):
    if l[y] == '#':
        return 1
    return 0

def countTrees(lines, xInc, yInc):
    rows = len(lines)
    y = 0
    x = 0 
    trees = 0
    while x < len(lines):
        trees = trees + isATree(lines[x],y )
        y = (y + yInc) % len(lines[x])
        x = x + xInc       
    return trees


if __name__ == "__main__":
  lines = []
  with open('input.txt', 'r') as f:
    for l in f:
      lines.append(l.strip())
  
  a = countTrees(lines, 1, 1)
  b = countTrees(lines, 1, 3)
  c = countTrees(lines, 1, 5)
  d = countTrees(lines, 1, 7)
  e = countTrees(lines, 2, 1)
  total = a * b * c * d * e
  print(f"There are {total} trees in your path.")

