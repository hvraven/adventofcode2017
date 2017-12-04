#!/usr/bin/env python3

import numpy as np

inp = 325489

a = np.arange(1, 1000, 2, dtype=np.uint64)
circle = np.searchsorted(a**2, inp)
steps = inp - a[circle - 1]**2
steps %= a[circle] - 1
hamming = circle + (a[circle] - 1) / 2 - steps
print(int(hamming))

memory = np.zeros((100,100), dtype=np.uint)
center = (50,50)
memory[center] = 1

pos = (50,50)

def next_pos(p):
    p = np.array(p)
    fc = p - center
    circle = np.max(np.abs(fc))
    if (fc[1] == circle):
        return tuple(p + (1,0))
    if (fc[0] == -circle):
        return tuple(p + (0,1))
    if (fc[1] == -circle):
        return tuple(p - (1,0))
    return tuple(p - (0,1))

while memory[pos] < inp:
    pos = next_pos(pos)
    x = pos[0]
    y = pos[1]
    memory[pos] = np.sum(memory[x-1:x+2, y-1:y+2])

print(memory[pos])
