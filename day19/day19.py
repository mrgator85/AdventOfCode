import re
def getValid(rules, r):
    valid = ['']
    if '|' in rules[r]:
        ret = []
        print(rules[r])
        for n in rules[r][:rules[r].index('|')]:
            for v in valid:
                for v1 in getValid(rules, int(n.strip())):
                    ret.append(v + v1)
        for n in rules[r][rules[r].index('|')+1:]:
            for v in valid:
                for v1 in getValid(rules, int(n.strip())):
                    ret.append(v + v1)
        valid = ret
    else:
        for rule in rules[r]:
            if(re.match(r'"(a|b)"', rule)):
                #return rule.strip('"')
                valid = [v + rule.strip('"') for v in valid]
            else:
                r = []
                for v in valid:
                    print(f"rule: {type(rule)}")
                    for v1 in getValid(rules, int(rule)):
                        r.append(v + v1)
                valid = r
    return valid





if __name__ == "__main__":
    test_rules = '0: 4 1 5\n1: 2 3 | 3 2\n2: 4 4 | 5 5\n3: 4 5 | 5 4\n4: "a"\n5: "b"'
    test_1 = '0: 4 1\n1: 4 | 5\n2: 4 4 | 5 5\n3: 4 5 | 5 4\n4: "a"\n5: "b"'
    rules = {}
    for l in test_rules.split('\n'):
        print(l)
        id, rule = l.strip().split(':')
        rules[int(id)] = rule.strip().split(' ')
    print(getValid(rules, 0))
