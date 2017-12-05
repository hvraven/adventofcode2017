#!/usr/bin/env python3

import numpy as np
from numba import jit

inp = np.genfromtxt('input', dtype=np.int32).flatten()

@jit
def part1(vec):
    i = 0
    pos = 0
    while pos < len(vec):
        vec[pos] += 1
        pos = pos + vec[pos] - 1
        i += 1
    print(i)

@jit
def part2(vec):
    i = 0
    pos = 0
    while pos < len(vec):
        opos = vec[pos]
        if vec[pos] >= 3:
            vec[pos] -= 1
        else:
            vec[pos] += 1
        pos = pos + opos
        i += 1
    print(i)

part1(inp.copy())
part2(inp.copy())
