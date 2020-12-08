
def readInput(path: str):
    f = open(path)
    groupAnswers = []
    groupAnswer = ""
    for line in f.readlines():
        if (line == "\n"):
            groupAnswers.append(groupAnswer)
            groupAnswer = ""
            continue
        groupAnswer += line.replace("\n", "")
    else:
        groupAnswers.append(groupAnswer)

    f.close()
    return groupAnswers

def solve(path: str):
    answers = readInput(path)
    res = 0
    for a in answers:
        distinct = set(a)
        # print(distinct)
        count = len(distinct)
        # print(count)
        res += count
    print(res)
    return res

solve('d6_inpt.txt')

def readInputPart2(path: str):
    f = open(path)
    groupAnswers = []
    groupAnswer = []
    for line in f.readlines():
        if (line == "\n"):
            groupAnswers.append(groupAnswer)
            groupAnswer = []
            continue
        groupAnswer.append(line.replace("\n", ""))
    else:
        groupAnswers.append(groupAnswer)

    f.close()
    return groupAnswers

def solvePart2(path: str):
    answers = readInputPart2(path)
    res = 0
    for answerList in answers:
        matches = set(answerList.pop(0))
        for answer in answerList:
            matches &= set(answer)
        count = len(matches)
        # print(count)
        res += count
    print(res)
    return res

solvePart2('d6_inpt.txt')