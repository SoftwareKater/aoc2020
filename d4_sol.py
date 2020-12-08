required = ["byr","ecl","eyr","hcl","hgt","iyr","pid"]

optional = ["cid"]

def readInput(path: str):
    f = open(path)
    passports = []
    rawPassport = ""
    for line in f.readlines():
        if (line == "\n"):
            passports.append(rawPassport)
            rawPassport = ""
            continue
        rawPassport += line.replace("\n", " ")
    f.close()
    return passports

def isValidPassport(passport):
    if passport.count(":") < 7:
        return False
    match = [key for key in required if key in passport]
    if len(match) < 7:
        # match.sort()
        # print(match)
        return False
    # for key in required:
    #     if not(key in passport):
    #         return False
    return True

def checkPassports(path: str):
    passports = readInput(path)
    validPassports = 0
    for p in passports:
        if isValidPassport(p):
            validPassports += 1
    return validPassports

print(checkPassports('d4_inpt.txt'))

