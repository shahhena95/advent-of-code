with open('./inputs/day_06.txt') as f:
    instructions = f.readlines()

instructions = [line.strip('\n').split() for line in instructions]

lights = [[False] * 1000 for i in range(1000)]


def process_input():
    #remove unwanted data
    for line in instructions:
        del line[line.index('through')]

    # modify on => True, off => False
    for line in instructions:
        if line[1] == 'on':
            line[1] = True
        if line[1] == 'off':
            line[1] = False

    #change to positions to integer
    for line in instructions:
        line[-1] = map(int, line[-1].split(','))
        line[-2] = map(int, line[-2].split(','))
    return instructions


def get_pos(instruction):
    return map(int, instruction.split(','))


def turn(switch, pos1, pos2):
    for i in range(pos1[0], pos2[0]+1):
        for j in range(pos1[1], pos2[1]+1):
            lights[i][j] = switch


def toggle(pos1, pos2):
    for i in range(pos1[0], pos2[0]+1):
        for j in range(pos1[1], pos2[1]+1):
            lights[i][j] = not lights[i][j]


def config_light():
    instructions = process_input()

    for line in instructions:
        if line[0] == 'turn':
            turn(line[1], line[-2], line[-1])
        else:
            toggle(line[-2], line[-1])

    print sum([item for sublist in lights for item in sublist])

config_light()
