#Referred to hints and solutions

import numpy as np
from scipy.ndimage import generic_filter


def state_of_light(neighbors):
    light = neighbors[4]
    on = np.sum(neighbors)
    if light:  # light is on
        if on == 3 or on == 4:  # 2 or 3 neighbors plus itself
            return 1
        else:
            return 0
    else:   # light is off
        if on == 3:
            return 1
        else:
            return 0


def take_steps(grid, steps):
    for i in range(steps):
        new_grid = generic_filter(
            grid, state_of_light, size=3, mode='constant')
        grid = new_grid
    return grid

input_grid = np.ones((100, 100), dtype='int')
for row_num, line in enumerate(open('inputs/day_18.txt')):
    row = [{'#': 1, '.': 0}[i] for i in line.strip()]
    input_grid[row_num, :] = row

# part a
grid = take_steps(input_grid, 100)
print np.sum(grid)


def partb():
    corners = { (0,0), (0,99), (99,0), (99,99) }
    with open('inputs/day_18.txt') as f:
        lights = corners | {(x, y) for y, line in enumerate(f)
                            for x, char in enumerate(line.strip())
                            if char == '#'}

        neighbours = lambda x, y: sum((_x, _y) in lights for _x in (x - 1, x, x + 1)
                                      for _y in (y - 1, y, y + 1) if (_x, _y) != (x, y))

        for c in xrange(100):
            lights = corners | {(x, y) for x in xrange(100) for y in xrange(100)
                                if (x, y) in lights and 2 <= neighbours(x, y) <= 3
                                or (x, y) not in lights and neighbours(x, y) == 3}
    return len(lights)

print partb()
