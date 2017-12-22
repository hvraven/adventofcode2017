#!/usr/bin/env python3

import numpy as np

with open('input', 'r') as f:
    inp = []
    for line in f.readlines():
        inp.append(np.fromstring(line.strip(), dtype=np.uint8))
inp = np.vstack(inp)

infected = np.zeros((1025,1025), dtype=bool)
infected[500:525,500:525] = inp == ord('#')

start = tuple(map(lambda x: x // 2, infected.shape))
print(start)

def left(direction):
    return -direction[1], direction[0]

def right(direction):
    return direction[1], -direction[0]

def burst(grid, pos, direction, count):
    if grid[pos]:
        direction = right(direction)
    else:
        count += 1
        direction = left(direction)

    grid[pos] = not grid[pos]
    pos = tuple(np.asarray(pos) + np.asarray(direction))
    return pos, direction, count

pos = start
direction = [-1, 0]
count = 0
for i in range(10000):
    pos, direction, count = burst(infected, pos, direction, count)
print(count)
