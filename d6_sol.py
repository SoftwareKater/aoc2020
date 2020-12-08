
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