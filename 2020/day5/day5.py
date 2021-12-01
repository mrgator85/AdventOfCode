import math

def search(s, minimum, maximum):
    mi = minimum
    ma = maximum
    for c in s:
        if(c == 'L' or c == 'F'): 
            ma = ma - math.floor((ma - mi)/2)
        else:
            mi = mi + math.ceil((ma - mi)/2)
    return mi
def findMySeat(a):
    a.sort()
    i = 1
    while(i < len(a) -1):
        if(a[i+1] != a[i]+1):
            # assuming there is only 1 open seat
            return a[i] + 1
        i = i + 1
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        sids = []
        for l in f:
            r = l.strip()[:7]
            s = l.strip()[7:]
            row = search(r, 0 , 127)
            seat = search(s, 0, 7)
            sids.append(row * 8 + seat)
        print(f"Max seat number is {max(sids)}")
        print(f"My seat is {findMySeat(sids)}")

    
     