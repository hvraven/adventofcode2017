#!/usr/bin/env python3

import numpy as np

with open('input', 'r') as f:
    inp = []
    for line in f.readlines():
        inp.append(np.fromstring(line.strip(), dtype=np.uint8))
inp = np.vstack(inp)

infected = np.zeros((100025,100025), dtype=np.uint8)
infected[50000:50025,50000:50025] = (inp == ord('#')) * 2

start = tuple(map(lambda x: x // 2, infected.shape))
print(start)

def left(direction):
    return -direction[1], direction[0]

def right(direction):
    return direction[1], -direction[0]

def reverse(direction):
    return -direction[0], -direction[1]

def burst(grid, pos, direction, count):
    if grid[pos] == 0:
        direction = left(direction)
    elif grid[pos] == 1:
        count += 1
    elif grid[pos] == 2:
        direction = right(direction)
    elif grid[pos] == 3:
        direction = reverse(direction)

    grid[pos] = (grid[pos] + 1) % 4
    pos = tuple(np.asarray(pos) + np.asarray(direction))
    return pos, direction, count

def doit(infected, pos):
    direction = [-1, 0]
    count = 0
    for i in range(10000000):
        if i % 100000 == 0:
            print(i)
        pos, direction, count = burst(infected, pos, direction, count)
    return count

print(doit(infected, start))
