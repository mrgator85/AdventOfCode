
def findPair(n, v):
    '''Checks to see if a pair exists in numbers n, that sums to v'''
    #print(n)
    a = [(x, y) for x in n for y in n if (x+y) == v]
    if (len(a) > 0):
        return True
    return False

def findContiguousSum(n, target):
    start = 0
    end = 1
    s = 0
    while(end < len(n)):
        while(s < target):
            s = sum(n[start:end])
            end = end + 1
        if(s == target):
            return start, end
        else:
            start = start + 1
            end = start+1
            s = 0

def findInvalid(n, s):
    '''finds the first number that is invalid in the set of n numbers for a buffer of s size
       for advent of code, small input is s=5, large input is s=25'''
    beg = 0
    end = s
    while(end+1 != len(n)):
        if(findPair(n[beg:end], n[end])):
            end = end + 1
            beg = beg + 1
        else:
            return n[end]

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        numbers = [int(x) for x in f]
        num = findInvalid(numbers, 25)
        print(num)
        s, e = findContiguousSum(numbers, num)
        print(f"{min(numbers[s:e]) + max(numbers[s:e])}")
