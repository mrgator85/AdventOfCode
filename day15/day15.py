def findNthSpoken(spoken, n):
    turn = 0
    while(turn < n):
        if(turn < len(spoken)):
            turn = turn + 1
        elif(turn == len(spoken)):
            if(spoken[turn-1] in spoken[:turn-1]):
                spoken.append(turn-1 - findLastIndexOf(spoken[:turn-1], spoken[turn-1]))
            else:
                spoken.append(0)
            turn = turn + 1
    return spoken[turn-1]

def findLastIndexOf(a, v):
    return len(a) - 1 - a[::-1].index(v)


if __name__ == "__main__":
    sample_input = [0, 3, 6]
    my_input = [8, 0, 17, 4, 1, 12]
    print(findNthSpoken(sample_input, 2020))
