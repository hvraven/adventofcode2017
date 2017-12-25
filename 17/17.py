#!/usr/bin/env python3

import numpy as np

inp = 394

def add_value(steps, buf, idx, value):
    pos = (idx + steps) % value
    np.roll(buf[pos:value+1], 1)
    buf[pos] = value
    return buf, pos + 1

def build_spinlock(steps, total=2018):
    buf = np.empty(total+1, dtype=np.uint32)
    buf[0] = 0
    length = 1
    idx = 0
    for i in range(1, total):
        if i % 100000 == 0:
            print(i)
        buf, idx = add_value(steps, buf, idx, i)
    return buf

l = build_spinlock(inp)
print(l[np.argwhere(l == 2017)[0,0] + 1])

pos = 0
for i in range(1, 50000000):
    if pos == 0:
        out = i
    pos = (pos + 1 + inp) % (i + 1)

print(out)

