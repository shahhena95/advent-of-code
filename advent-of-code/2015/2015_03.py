with open('./inputs/day_03.txt') as f:
    instructions = f.readlines()


def part1():
    X = Y = 0
    visited = [(0, 0)] #(0,0) always visited
    unique_houses_visited = 1 #house at (0,0)

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

# part1()


def is_new_house(X, Y, visited):
    if (X, Y) not in visited:
        # New house
        visited.append((X, Y))
        return 1
    return 0


def part2():
    santaX = santaY = 0
    roboX = roboY = 0
    visited = [(0,0)] #(0,0) always visited
    unique_houses_visited = 1 #house at (0,0) visited by Santa and Robo-santa
    santasTurn = True

    for c in instructions[0]:
        if c == '^':
            santaY += int(santasTurn)
            roboY += int(not santasTurn)

        elif c == '<':
            santaX -= int(santasTurn)
            roboX -= int(not santasTurn)
        elif c == 'v':
            santaY -= int(santasTurn)
            roboY -= int(not santasTurn)
        elif c == '>':
            santaX += int(santasTurn)
            roboX += int(not santasTurn)

        if santasTurn:
            unique_houses_visited += is_new_house(santaX, santaY, visited)
        else:
            unique_houses_visited += is_new_house(roboX, roboY, visited)

        santasTurn = not santasTurn


    print unique_houses_visited

part2()
