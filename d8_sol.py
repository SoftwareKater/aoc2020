class CodeLine:
    def __init__(self, operation: str, argument: int, visited: bool):
        self.visited = visited
        self.operation = operation
        self.argument = argument
    def __repr__(self):
        return ' '.join([self.operation, str(self.argument)])

def readInput(path: str):
    f = open(path)
    program = []
    for line in f.readlines():
        op = line[:3]
        arg = int(line[4:])
        cl = CodeLine(op, arg, False)
        program.append(cl)
    f.close()
    return program

def solve(path: str):
    program = readInput(path)
    print(program)
    accumulator = 0
    head = 0
    halt = False
    while not halt:
        print(accumulator)
        print(head)
        print('---')
        line = program[head]
        if line.visited:
            halt = True
            continue
        if line.operation == 'acc':
            accumulator += line.argument
            head += 1
            line.visited = True
        elif line.operation == 'nop':
            head += 1
            line.visited = True
        elif line.operation == 'jmp':
            head += line.argument
            line.visited = True
    print(accumulator)

print('*** PART 1 ***')
solve('d8_inpt.txt')
print()


# print('*** PART 2 ***')
# solvePart2('d7_inpt_test.txt')
