import numpy as np

with open('./input_21.txt') as f:
    instructions = f.readlines()

mappings = {}
start = '.#./..#/###'


def translate_to_np(s):
    return np.array([[c == '#' for c in l]
                     for l in s.split('/')])

for line in instructions:
    k, v = map(translate_to_np, line.strip().split(' => '))
    for a in (k, np.fliplr(k)):
        for r in range(4):
            mappings[np.rot90(a, r).tostring()] = v


def find_next(grid):
    size = len(grid)
    by = 2 if size % 2 == 0 else 3
    new_size = size * (by+1) // by
    new_grid = np.empty((new_size, new_size), dtype=bool)
    squares = range(0, size, by)
    new_squares = range(0, new_size, by+1)
    for i, ni in zip(squares, new_squares):
        for j, nj in zip(squares, new_squares):
            square = grid[i:i+by, j:j+by]
            enhanced = mappings[square.tostring()]
            new_grid[ni:ni+by+1, nj:nj+by+1] = enhanced
    return new_grid


grid = translate_to_np(start)
for _ in range(5):
    grid = find_next(grid)
print(grid.sum())

grid = translate_to_np(start)
for _ in range(18):
    grid = find_next(grid)
print(grid.sum())
