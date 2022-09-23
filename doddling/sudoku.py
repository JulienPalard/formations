import numpy as np
from collections import Counter


def is_done(grid):
    for square in (
        grid[0:3, 0:3],
        grid[0:3, 3:6],
        grid[0:3, 6:9],
        grid[3:6, 0:3],
        grid[3:6, 3:6],
        grid[3:6, 6:9],
        grid[6:9, 0:3],
        grid[6:9, 3:6],
        grid[6:9, 6:9],
    ):
        if set(square.ravel()) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return False
    for line in grid:
        if set(line) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return False
    for line in grid.T:
        if set(line) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            return False
    return True


def is_valid(grid):
    for square in (
        grid[0:3, 0:3],
        grid[0:3, 3:6],
        grid[0:3, 6:9],
        grid[3:6, 0:3],
        grid[3:6, 3:6],
        grid[3:6, 6:9],
        grid[6:9, 0:3],
        grid[6:9, 3:6],
        grid[6:9, 6:9],
    ):
        c = Counter(square.ravel())
        if 0 in c:
            del c[0]
        try:
            value, occurences = c.most_common(1)[0]
            if occurences > 1:
                return False
        except IndexError:
            pass
    for line in grid:
        c = Counter(line)
        if 0 in c:
            del c[0]
        try:
            value, occurences = c.most_common(1)[0]
            if occurences > 1:
                return False
        except IndexError:
            pass
    for line in grid.T:
        c = Counter(line)
        if 0 in c:
            del c[0]
        try:
            value, occurences = c.most_common(1)[0]
            if occurences > 1:
                return False
        except IndexError:
            pass
    return True


grid = np.zeros((9, 9), dtype=int)
grid = np.array(
    [
        [0, 0, 0, 1, 1, 1, 2, 2, 2],
        [0, 0, 0, 1, 1, 1, 2, 2, 2],
        [0, 0, 0, 1, 1, 1, 2, 2, 2],
        [3, 3, 3, 4, 4, 4, 5, 5, 5],
        [3, 3, 3, 4, 4, 4, 5, 5, 5],
        [3, 3, 3, 4, 4, 4, 5, 5, 5],
        [6, 6, 6, 7, 7, 7, 8, 8, 8],
        [6, 6, 6, 7, 7, 7, 8, 8, 8],
        [6, 6, 6, 7, 7, 7, 8, 8, 8],
    ]
)
is_valid(grid)


def find_first_blank(grid):
    i, j = 0, 0
    for i in range(9):
        for j in range(9):
            if grid[i, j] == 0:
                return i, j


def solve(grid):
    print(grid)
    if is_done(grid):
        print(grid)
        exit(0)
    try:
        my_i, my_j = find_first_blank(grid)
    except TypeError:
        return
    for i in range(1, 10):
        grid[my_i, my_j] = i
        if is_valid(grid):
            solve(grid.copy())


grid = np.array(
    [
        [0, 0, 0, 7, 3, 0, 6, 0, 0],
        [0, 7, 0, 0, 8, 0, 1, 5, 0],
        [2, 3, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 2, 4, 0, 5],
        [6, 4, 0, 0, 0, 0, 0, 8, 2],
        [5, 0, 9, 3, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 4, 8],
        [0, 9, 4, 0, 2, 0, 0, 7, 0],
        [0, 0, 5, 0, 7, 6, 0, 0, 0],
    ]
)


solve(grid)
