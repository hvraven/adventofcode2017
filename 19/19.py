#!/usr/bin/env python3

import numpy as np

with open('input', 'r') as f:
    inp = map(lambda x: np.fromstring(x, dtype=np.uint8),
              f.readlines())
    inp = np.vstack(inp)

print(inp.shape)

def move(grid, pos, direction):
    pos[0] += direction[0]
    pos[1] += direction[1]
    if grid[pos] == ord('+'):
        if direction[0] == 0:
            if grid[pos[0] - 1, pos[1]] != ord(' '):
                return pos, [-1, 0], ''
            else:
                return pos, [1, 0], ''
        if direction[1] == 0:
            if grid[pos[0], pos[1] - 1] != ord(' '):
                return pos, [0, -1], ''
            else:
                return pos, [0, 1], ''

    if grid[pos] != ord('|') and grid[pos] != ord('-'):
        if grid[pos] == ord(' '):
            return pos, 0, ''  # end
        return pos, direction, chr(grid[pos])
    return pos, direction, ''


def find_path(grid):
    pos = [0, np.where(grid[0] == ord('|'))[0]]
    direction = [1, 0]
    out = ''
    count = 0
    while direction:
        pos, direction, o = move(grid, pos, direction)
        out += o
        count += 1

    return out, count


print(find_path(inp))
