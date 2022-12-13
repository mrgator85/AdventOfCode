class Monkey(object):
    def __init__(self, items = [], op = '', test = '', true_dest = 0, false_dest = 0  ):
        self.items = items
        self.op = op
        self.testval = int(test)
        self.true_dest = true_dest
        self.false_dest = false_dest
        self.inspection = 0
    def test(self, v):
        return 0 == v % self.testval
    
    def operation(self, v):
        t, o, x = self.op.split()
        if(x == 'old'):
            x = v
        else: 
            x = int(x)
        if(o == '+'):
            return int(v + x)
        if(o == '*'):
            return int(v * x)
        else:
            return int(v - x)

    def turn(self):
        self.inspection = self.inspection + 1
        item = self.items.pop(0)
        item = self.operation(item)
        item = int(item / 3)
        if(self.test(item)):
            return(item, self.true_dest)
        else:
            return(item, self.false_dest)

    def add_item(self,item):
        self.items.append(item)



monkeys = []
# monkeys.append(Monkey([79, 98], 'old * 19', 23, 2, 3))
# monkeys.append(Monkey([54,65,75,74], 'old + 6', 19, 2, 0))
# monkeys.append(Monkey([79,60,97], 'old * old', 13, 1, 3))
# monkeys.append(Monkey([74], 'old + 3', 17, 0,1))

monkeys.append(Monkey([72,64,51,57,93,97,68], 'old * 19', 17, 4,7))
monkeys.append(Monkey([62], 'old * 11', 3, 3,2))
monkeys.append(Monkey([57, 94, 69, 79, 72], 'old + 6', 19, 0,4))
monkeys.append(Monkey([80,64,92,93,64,56], 'old + 5', 7, 2,0))
monkeys.append(Monkey([70,88,95,99,78,72,65,94], 'old + 7', 2, 7,5))
monkeys.append(Monkey([57,95,81,61], 'old * old', 5, 1,6))
monkeys.append(Monkey([79,99], 'old + 2', 11, 3,1))
monkeys.append(Monkey([68, 98, 62], 'old + 3', 13, 5,6))
for i in range(20):
    for m in monkeys:
        while(m.items):
            (i, d) = m.turn()
            monkeys[d].add_item(i)

for m in monkeys:
    print(m.inspection)

print(monkeys)
