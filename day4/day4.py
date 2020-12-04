import re
## validates that required fields are present
### doc is a dictionary of field : values
### returns boolean
rules = { 'byr' : lambda x : int(x) >= 1920 and int(x) <= 2002,
          'iyr' : lambda x : int(x) >= 2010 and int(x) <= 2020,
          'eyr' : lambda x : int(x) >= 2020 and int(x) <= 2030,
          'hgt' : lambda y : True if len([x for x in re.findall(r'(\d+)(in|cm)', y) if (int(x[0]) >= 150 and int(x[0]) <= 193 and x[1]=='cm') or (int(x[0]) >= 59 and int(x[0]) <= 76 and x[1] == 'in')]) > 0 else False,
          'hcl' : lambda x : len(re.findall(r'#[0-9a-f]{6}', x)) > 0,
          'ecl' : lambda x : len(re.findall(r'(amb|blu|brn|gry|grn|hzl|oth)', x)) > 0,
          'pid' : lambda x : len(re.findall(r'^[0-9]{9}$', x)) > 0,
          'cid' : lambda x : True
}

def validate(doc):
    """validate - validates that a passport has required fields
       @param doc - a dictionary of field : value pairs
       @return boolean - True if valid, False if invalid 
    """
    reqFields = set(['byr', 'iyr','eyr','hgt','hcl','ecl','pid'])
    #Rapid check, the minimum number of valid fields is 7
    if(len( doc.keys()) < 7):
        return False
    if(reqFields.issubset(set(doc.keys()))):
        return True
    return False

def validate2(doc):
    """validate - validates that a passport has required fields
       @param doc - a dictionary of field : value pairs
       @return boolean - True if valid, False if invalid 
    """
    reqFields = set(['byr', 'iyr','eyr','hgt','hcl','ecl','pid'])
    #Rapid check, the minimum number of valid fields is 7
    if(len( doc.keys()) < 7):
        return False
    if(reqFields.issubset(set(doc.keys()))):
        for k in doc.keys():
            if not rules[k](doc[k]):
                return False
        return True
    return False

with open('input.txt', 'r') as f:
    doc = {}
    validCount = 0
    for l in f:
        if(len (l.strip()) == 0):
            if(validate2(doc)):
                validCount = validCount + 1
            doc.clear()
        else:
            for p in [x.strip() for x in l.split(' ')]:
                k, v = p.split(':')
                doc[k.strip()] = v.strip()
    # validate the final passport
    if(validate2(doc)):
        validCount = validCount + 1
    print(f"There are {validCount} valid IDs.")

