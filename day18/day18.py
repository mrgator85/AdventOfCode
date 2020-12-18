import re
def evaluate(s):
    
    op = '+'
    counter = 0
    c = next(prob, 'end')
    
    while(c != 'end' ):
        print(f"c: |{c}|") 
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

if __name__ == "__main__":
    s = '6 + ((7 * 2) + 4)'
    with open('input.txt', 'r') as f:
        total = 0
        for s in f:
            prob = iter([a for a in list(s.strip()) if a != ' '])
            total = total + evaluate(prob)
        print(total)
    #prob = iter([a for a in list(s) if a != ' '])
    #print(evaluate(prob))