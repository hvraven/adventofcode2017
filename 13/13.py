#!/usr/bin/env python3

import numpy as np
from numba import jit

inp = np.genfromtxt('input', delimiter=': ', dtype=np.int).T
state = np.zeros(int(1 + inp[0,-1]))
depth = np.ones_like(state, dtype=np.int) * 2 * len(state)
depth[inp[0]] = inp[1]


def move(state, pos):
    penalty = 0
    if state[pos] % (2 * depth[pos] - 2) == 0:
        penalty = pos * depth[pos]

    state += 1

    return penalty

def run(state):
    return np.add.reduce(list(map(lambda p: move(state, p),
                                  range(len(state)))))

print(run(state.copy()))

idx = inp[0]
depth = inp[1]

@jit
def hide():
    delay = 0
    while True:
        if not np.any((idx + delay) % (2 * depth - 2) == 0):
            return delay
        delay += 1

print(hide())
