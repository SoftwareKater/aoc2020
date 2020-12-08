def readInput(path: str):
    f = open(path)
    content = f.readlines()
    f.close
    return content

def solve(path: str, dx: int, dy: int = 1):
    treeMap = readInput(path)
    lineLen = len(treeMap[0]) - 1
    
    treeHits = 0
    posX = 0
    posY = 0
    while posY < len(treeMap):
        line = treeMap[posY]
        if isTree(line, posX):
            treeHits += 1
        posX = (posX + dx) % lineLen
        posY += dy
    
    return treeHits

def isTree(line, poxX):
    return line[poxX] == '#'

SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

res = 1
for pos in SLOPES:
    res *= solve('d3_inpt.txt', pos[0], pos[1])
print(res)
# print(solve('d3_inpt.txt', 3))