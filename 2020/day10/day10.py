
class Counter(object):
    def __init__(self, initValue=0):
        self.v = initValue; 
    def inc(self, val=1):
        self.v = self.v + val 
        return self.v

def foo(adapters):
    
    ones = 0
    threes = 0
    for a in range(len(adapters)-1):
        if(adapters[a+1] - adapters[a] == 1):
            ones = ones + 1
        elif(adapters[a+1] - adapters[a] == 3):
            threes = threes + 1
    print(f"answer: {ones * threes}")

def bar(adapters, n, counter, memo):
    if(n in memo.keys()):
        counter.inc(memo[n])
    else:
        c = counter.v
        if(adapters[n] == max(adapters)):
            counter.inc(1)
        else:
            for i in range(n+1, n+4, 1):
                if(i < len(adapters)):
                    if(adapters[i] < adapters[n] + 4):
                        bar(adapters, i, counter, memo)
        memo[n] = counter.v - c 


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        a = [int(n) for n in f.readlines()]
        a.append(0)
        a.append(max(a)+3)
        a.sort()
        foo(a)
        memo = {}
        counter = Counter()
        bar(a, 0, counter, memo)
        print(counter.v)