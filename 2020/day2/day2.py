
##4-6 b: bbbdbtbbbj
##1-6 g: ggvggbgggstg
def validate(pw):
    rule, password = pw.split(':')
    r, letter = rule.split(' ')
    mini, maxi = r.split('-')
    c = password.count(letter)
    if(c >= int(mini) and c <= int(maxi)):
        return True
    return False

def validate2(pw):
    rule, password = [a.strip() for a in pw.split(':')]
    r, letter = rule.split(' ')
    pos1, pos2 = [int(a)-1 for a in r.split('-')]
    if((password[pos1] == letter) != (password[pos2] == letter)):
        return True
    return False

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        valid1 = 0
        valid2 = 0
        for l in lines:
            if validate(l):
                valid1 = valid1 + 1
            if validate2(l):
                valid2 = valid2 + 1
        print(f"There are {valid1} valid passwords.")
        print(f"There are {valid2} valid passwords.")