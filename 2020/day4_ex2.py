import sys, re
f = open("%s_input.txt" % sys.argv[0].split('_')[0], "r")

log = True

def checkByr(passport):
    if 'byr' in passport and 1920 <= int(passport['byr']) <= 2002:
        return True
    elif log:
        print('byr ko', passport)
    return False    

def checkIyr(passport):
    if 'iyr' in passport and 2010 <= int(passport['iyr']) <= 2020:
        return True
    elif log:
        print('iyr ko', passport)
    return False

def checkEyr(passport):
    if 'eyr' in passport and 2020 <= int(passport['eyr']) <= 2030:
        return True
    elif log:
        print('eyr ko', passport)
    return False

def checkHgt(passport):
    if ('hgt' in passport and ((passport['hgt'].endswith('cm') and 150 <= int(passport['hgt'].split('cm')[0]) <= 193)
            or (passport['hgt'].endswith('in') and 59 <= int(passport['hgt'].split('in')[0]) <= 76))):
        return True
    elif log:
        print('hgt ko', passport)
    return False

def checkHcl(passport):
    if 'hcl' in passport and re.match('^#[0-9a-f]{6}$', passport['hcl']):
        return True
    elif log:
        print('hcl ko', passport)
    return False

def checkEcl(passport):
    if 'ecl' in passport and passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl','oth']:
        return True
    elif log:
        print('ecl ko', passport)
    return False

def checkPid(passport):
    if 'pid' in passport and re.match('^[0-9]{9}$', passport['pid']):
        return True
    elif log:
        print('pid ko', passport)
    return False

def check(passport):
    result = (checkByr(passport)
        and checkIyr(passport)
        and checkEyr(passport)
        and checkHgt(passport)
        and checkHcl(passport)
        and checkEcl(passport)
        and checkPid(passport))
    if log:
        print(result, passport)
    return result

valid = 0
passport = dict()
for line in f:    
    if line == "\n":
        if check(passport):
            print(passport['hgt'])
            valid += 1
        passport = dict()
    else:
        for field in line.rstrip().split(" "):
            (key, value) = field.split(":")
            if key != "cid":
                passport[key] = value

if check(passport):
    #print(passport['hgt'])
    valid += 1

print(valid)