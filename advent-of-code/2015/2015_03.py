with open('./inputs/day_03.txt') as f:
    instructions = f.readlines()


def part1():
    X = Y = 0
    visited = [(0, 0)]
    unique_houses_visited = 1

    for c in instructions[0]:
        if c == '^':
            Y += 1
        elif c == '<':
            X -= 1
        elif c == 'v':
            Y -= 1
        elif c == '>':
            X += 1

        if (X, Y) not in visited:
            unique_houses_visited += 1
            visited.append((X, Y))

    print unique_houses_visited

part1()


def is_new_house(X, Y, visited):
    if (X, Y) not in visited:
        # New house
        visited.append((X, Y))
        return 1
    return 0


def part2():
    santa_x = santa_y = 0
    robo_x = robo_y = 0
    visited = [(0, 0)]
    unique_houses_visited = 1
    santas_turn = True

    for c in instructions[0]:
        if c == '^':
            santa_y += int(santas_turn)
            robo_y += int(not santas_turn)

        elif c == '<':
            santa_x -= int(santas_turn)
            robo_x -= int(not santas_turn)
        elif c == 'v':
            santa_y -= int(santas_turn)
            robo_y -= int(not santas_turn)
        elif c == '>':
            santa_x += int(santas_turn)
            robo_x += int(not santas_turn)

        if santas_turn:
            unique_houses_visited += is_new_house(santa_x, santa_y, visited)
        else:
            unique_houses_visited += is_new_house(robo_x, robo_y, visited)

        santas_turn = not santas_turn

    print unique_houses_visited

part2()
