import re
def evaluate(prob):
    
    op = '+'
    counter = 0
    c = next(prob, 'end')
    
    while(c != 'end' ):
        if(c in ['+', '*']):
            op = c 
        elif(c == '('):
            v = evaluate(prob)
        elif(c == ')'):
            return counter
        else:
            v = int(c)
        if(c in ['+', '*']):
            op = c
        elif(op == '*'):
            counter = counter * v
        else:
            counter = counter + v
        c = next(prob, 'end')
    return counter
def evaluate2(prob):
    op = '+'
    counter = 0
    c = next(prob, 'end')
    while(c != 'end' ):
        if(c in ['+', '*']):
            op = c 
        elif(c == '('):
            v = evaluate2(prob)
        elif(c == ')' or c == '*'):
            return counter
        else:
            v = int(c)
        if(c in ['+']):
            op = c
        elif(c == '*'):
            #counter = counter * evaluate2(prob)
            return counter * evaluate2(prob)
        else:
            counter = counter + v
        c = next(prob, 'end')
    return counter

if __name__ == "__main__":
    s = '6 + ((7 * 2) + 4)'
    with open('input.txt', 'r') as f:
        total1 = 0
        total2 = 0
        for s in f:
            prob1 = iter([a for a in list(s.strip()) if a != ' '])
            prob2  = iter([a for a in list(s.strip()) if a != ' '])
            total1 = total1 + evaluate(prob1)
            total2 = total2 + evaluate2(prob2)
        print(total1)
        print(total2)
    #prob = iter([a for a in list(s) if a != ' '])
    #print(evaluate(prob))