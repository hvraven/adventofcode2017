#!/usr/bin/env python3

import numpy as np

inp = np.genfromtxt('input', dtype=np.uint8)

def reallocation(vec):
    seen = set()
    i = 0

    while tuple(vec) not in seen:
        seen.add(tuple(vec))
        pos = np.argmax(vec)
        count = vec[pos]
        vec[pos] = 0
        while count > 0:
            pos += 1
            pos %= len(vec)
            vec[pos] += 1
            count -= 1
        i += 1

    print(i)

    seen = vec.copy()
    i = 0

    while True:
        pos = np.argmax(vec)
        count = vec[pos]
        vec[pos] = 0
        while count > 0:
            pos += 1
            pos %= len(vec)
            vec[pos] += 1
            count -= 1
        i += 1
        if np.all(seen == vec):
            break

    return i

print(reallocation(inp.copy()))
