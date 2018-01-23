with open('inputs/day_23.txt') as f:
    instructions = f.readlines()

instructions = [line.split() for line in instructions]


def process_turing(part2=False):
    registers = {'a': 0, 'b': 0}
    offset = 0
    if part2:
        registers['a'] = 1

    while offset < len(instructions):
        current = instructions[offset]

        if current[0] == 'hlf':
            registers[current[1]] /= 2

        elif current[0] == 'tpl':
            registers[current[1]] *= 3

        elif current[0] == 'inc':
            registers[current[1]] += 1

        elif current[0] == 'jmp':
            offset += int(current[1])
            continue

        elif current[0] == 'jie':
            if registers[current[1].strip(',')] % 2 == 0:
                offset += int(current[-1])
                continue

        elif current[0] == 'jio':
            if registers[current[1].strip(',')]  == 1:
                offset += int(current[-1])
                continue

        offset += 1
    return registers['b']


print process_turing()
print process_turing(part2=True)
