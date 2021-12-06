class Card(object):
    def __init__(self, c):
        self.card = []
        for r in c:
            self.card.append([[int(v.strip()), False] for v in r.strip().split()])

    def playNumber(self, n):
        for r in self.card:
            try:
                i = [n[0] for n in r].index(n)
                r[i][1] = True
            except(ValueError):
                pass

    def checkRow(self, r):
        #print(r)
        for v in r:
            if(v[1] == False):
                return False
        return True
    def checkRows(self):
        
        for r in self.card:
            if(self.checkRow(r)):
                return True
        return False
            
    def checkColumns(self):
        for i in range(5):
            if(self.checkRow([n[i] for n in self.card])):
                return True
        return False
            

    def isWinner(self):
        if(self.checkRows()):
            return True
        if(self.checkColumns()):
            return True
        return False

    def sumUnmarked(self):
        s = 0
        for r in self.card:
            for v in r:
                if(v[1] == False):
                    s = s + v[0]
        return s
    def print(self):
        print('----------')
        for r in self.card:
            print(r)
        print('----------')



# get 5 lines
def takeFive(lines):
    return lines[0:5], lines[5:]



#plays = [1,2,3,4,5,6,7]
# card_in = ["22 13 17 11  0",
#            " 3  2 5  4 6",
#            "21  9 14 16  7",
#             "6 10  3 18  5",
#             " 1 12 20 15 19"]
# card_in = ["22 13 17 3  0",
#            " 32  22 52  4 62",
#            "21  9 14 5  7",
#             "69 10  3 6  53",
#             " 1 12 20 7 19"]
# card = Card(card_in)
# for v in plays:
#     card.playNumber(v)
#     print(card.checkColumns())
# card.print()

with open("input.txt", "r") as f:
    calls = [int(x) for x in f.readline().split(',')]
    lines = [x.strip() for x in f.readlines() if x != '\n']
    cards = []
    while(len(lines) > 0):
        card, lines = takeFive(lines)
        cards.append(Card(card))
    finished = False
    for v in calls:
        if not finished:
            for c in cards:
                c.playNumber(v)
                if(c.isWinner()):
                    print("Winner is Found")
                    c.print()
                    print(v * c.sumUnmarked())
                    finished = True
                    break
        else:
            break


    

