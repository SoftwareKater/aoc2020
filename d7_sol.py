
def readInput(path: str):
    f = open(path)
    rules = {}
    for line in f.readlines():
        rule = {}
        bagDefEndIdx = line.find('contain')
        bagDef = line[:bagDefEndIdx].strip().rstrip('s')
        rules[bagDef] = rule
        bagContainsRaw = line[bagDefEndIdx + len('contain') + 1 : ]
        bagContainsListRaw = bagContainsRaw.split(', ')
        for content in bagContainsListRaw:
            content = content.strip().strip('.').rstrip('s')
            splitIdx = content.find(' ')
            count = content[: splitIdx + 1]
            if count == 'no ':
                count = 0
            else:
                count = int(count)
            bag = content[splitIdx + 1:]
            rule[bag] = count
    f.close()
    return rules

def solve(path: str):
    rules = readInput(path)
    # print(rules)
    myBag = 'shiny gold bag'
    res = set([myBag])
    oldRes = set()
    while res != oldRes:
        oldRes = res.copy()
        for container, contentDict in rules.items():
            for content, count in contentDict.items():
                if content in res and count > 0:
                    res.add(container)
    res.remove(myBag)
    # print(res)
    print(len(res))

print('*** PART 1 ***')
solve('d7_inpt.txt')
print()

from functools import reduce

def solvePart2(path: str):
    rules = readInput(path)
    bags = {}
    dig = {'shiny gold bag': 1}

    while dig:
        print('---')
        print(bags)
        print(dig)
        newDig = {}
        for container, countContainer in dig.items():
            if container in bags:
                bags[container] += countContainer
            else:
                bags[container] = countContainer
            for content, countContent in rules[container].items():
                if content == 'other bag' or countContent == 0:
                    continue
                if content in newDig:
                    newDig[content] += countContainer * countContent
                else:
                    newDig[content] = countContainer * countContent

        dig = dict(newDig)
    print('======')
    print(bags)
    res = reduce(lambda x, y: x+y, bags.values()) - 1
    print(res)

print('*** PART 2 ***')
solvePart2('d7_inpt.txt')
