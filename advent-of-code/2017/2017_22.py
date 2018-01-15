with open('./input_22.txt') as f:
    instructions = f.readlines()


#took hint from reddit
def sporifica_virus(part):
    grid = {}
    x = len(instructions) // 2
    position = (x + len(instructions[0].strip())//2 * 1j)
    direction = -1
    infected = 0
    #improved coding style
    for i, line in enumerate(instructions):
        for j, char in enumerate(line.strip()):
            grid[(i + j*1j)] = 0 if char == '.' else part

    bursts = {1: 10000, 2: 10000000}
    # 1: infected, 2: weakened , 3: flagged, 0: clean
    for _ in range(bursts[part]):
        status = grid.get(position, 0)

        if part == 1:
            if status == 0:
                infected += 1
            direction *= (1 - 2 * status) * 1j

        else:
            if status == 1:
                infected += 1
            elif status == 2:
                direction *= -1j
            elif status == 3:
                direction *= -1
            else:
                direction *= 1j

        grid[position] = (status + 1) % (2 * part)
        position += direction

    return infected

print(sporifica_virus(part=1))
print(sporifica_virus(part=2))
