def readInput(path: str):
    f = open(path)
    content = f.readlines()
    f.close
    return content

def getSeatIDs():
    inpt = readInput('d5_inpt.txt')
    seatIDs = []
    for seat in inpt:
        row = getRow(seat)
        column = getColumn(seat)
        seatIDs.append(8*row + column)
    return seatIDs

def getRow(code: str):
    code = code[:7]
    code = code.replace("B", "1").replace("F", "0")
    row = 0
    for i in range(7):
        row += 2**i * int(code[6-i])
    return row

def getColumn(code: str):
    code = code[7:]
    code = code.replace("L", "0").replace("R", "1")
    column = 0
    for i in range(3):
        column += 2**i * int(code[2-i])
    return column

def getMySeat():
    seatIDs = getSeatIDs()
    found = False
    seat = None
    key = 1
    while not found:
        # bullshit
        if int(seatIDs[key - 1], 8) == int(seatIDs[key + 1] + 2, 8):
            found = True
            print(key)
            print(seatIDs[key])
        key += 1

# def getNextSeatID(seatID):
#     seatIDstr = str(seatID)
#     column = int(seatIDstr[:-1]) / 8
#     row = int(seatIDstr[-1])
#     print(column)
#     print(row)
#     resColumn = 0
#     if (row < ):
#         resRow = int(row)
#     else:
#         resRow = 0

# seatIDs = getSeatIDs()
# print(max(seatIDs))
print(getMySeat())
# print(getNextSeatID('BBBBBBBRRR'))