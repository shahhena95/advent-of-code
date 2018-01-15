with open('./inputs/day_06.txt') as f:
    instructions = f.readlines()

instructions = [line.strip('\n').split() for line in instructions]

switch_ancient = {'on': True, 'off': False}
switch = {'on': 1, 'off': -1}


def process_input():
    #remove unwanted data
    for line in instructions:
        del line[line.index('through')]

    #change to positions to integer
    for line in instructions:
        line[-1] = map(int, line[-1].split(','))
        line[-2] = map(int, line[-2].split(','))
    return instructions

instructions = process_input()


def turn_ancient(lights, switch_action, pos1, pos2):
    for i in range(pos1[0], pos2[0]+1):
        for j in range(pos1[1], pos2[1]+1):
            lights[i][j] = switch_ancient[switch_action]


def toggle_ancient(lights, pos1, pos2):
    for i in range(pos1[0], pos2[0]+1):
        for j in range(pos1[1], pos2[1]+1):
            lights[i][j] = not lights[i][j]


def config_light_ancient():
    lights = [[False] * 1000 for i in range(1000)]
    for line in instructions:
        if line[0] == 'turn':
            turn_ancient(lights, line[1], line[-2], line[-1])
        else:
            toggle_ancient(lights, line[-2], line[-1])

    print sum([item for sublist in lights for item in sublist])


config_light_ancient()


def turn(lights, switch_action, pos1, pos2):
    for i in range(pos1[0], pos2[0]+1):
        for j in range(pos1[1], pos2[1]+1):
            if lights[i][j] + switch[switch_action] > 0:
                lights[i][j] += switch[switch_action]
            else:
                lights[i][j] = 0


def toggle(lights, pos1, pos2):
    for i in range(pos1[0], pos2[0]+1):
        for j in range(pos1[1], pos2[1]+1):
            lights[i][j] += 2


def config_light():
    lights = [[False] * 1000 for i in range(1000)]
    for line in instructions:
        if line[0] == 'turn':
            turn(lights, line[1], line[-2], line[-1])
        else:
            toggle(lights, line[-2], line[-1])

    print sum([item if item > 0 else 0 for sublist in lights for item in sublist])

config_light()
