# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.

##Sample 
# [({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]

# will have 5 illegal lines
# {([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
# [[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
# [{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
# [<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
# <{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.

# first illegal character in a line and look up value - add them up score should be 26397
values = {')': 3, ']':57, '}':1197, '>':25137}
finishScores = {'(': 1, '[':2, '{':3, '<':4}
def checkLine(l):
    chars = []
    valid = True
    expected = 'a'
    got = 'a'
    for c in l:
        if c == '[' or c == '{' or c == '(' or c == '<':
            chars.append(c)
        elif c == ']':
            tc = chars.pop()
            if tc != '[':
                print("Found ] expected {}".format(tc))
                return values[c]
        elif c == '}':
            tc = chars.pop()
            
            if tc != '{':
                print("Found expected {}".format(tc))
                return values[c]
        elif c == ')':
            tc = chars.pop()
            
            if tc != '(':
                print("Found ) expected {}".format(tc))
                return values[c]
        elif(c == '>'):
            tc = chars.pop()
            
            if tc != '<':
                print("Found > expected {}".format(tc))
                return values[c]
    return 0

#print(checkLine('[({(<(())[]>[[{[]{<()<>>'))
# print(checkLine('[(])'))
# print(checkLine('{([(<{}[<>[]}>{[]{[(<()>'))
def getFinishScore(l):
    chars = []
    for c in l:
        if c == '[' or c == '{' or c == '(' or c == '<':
            chars.append(c)
        else:
            chars.pop()
    print(chars)
    score = 0
    #for c in chars:
    while(len(chars) > 0):
        score = score * 5
        score = score + finishScores[chars.pop()]
    print(score)
    return score

with open("input.txt", "r") as f:
    s = 0
    validlines = []
    fscores = []
    for l in f.readlines():
        v = checkLine(l.strip())
        if(v == 0):
            validlines.append(l)
        s = s + v
    for l in validlines:
        fscores.append(getFinishScore(l.strip()))
    print(fscores)
    fscores.sort()
    mid = int(len(fscores)/2)

    print(s)
    print(fscores[mid])
