#!/usr/bin/env python3

import numpy as np

def knot_hash(string):
    inp = np.fromstring(string, dtype=np.uint8)
    inp = np.concatenate((inp, [17, 31, 73, 47, 23]))
    sparse = run_sequence(inp, rounds=64)
    return np.bitwise_xor.reduce(sparse.reshape((16,16)), axis=1)


def run_sequence(seq, rounds=1):
    clist = np.arange(0, 256, dtype=np.uint8)
    pos = 0
    skip = 0

    for i in range(rounds):
        clist, pos, skip = round(seq, clist, pos, skip)

    return clist

def round(seq, clist, pos, skip):
    for length in seq:
        r = range(pos, pos + length)
        vals = clist.take(r , mode='wrap')
        clist.put(r, np.flip(vals, 0), mode='wrap')
        pos += length + skip
        skip += 1
    return clist, pos, skip

def make_grid(inp):
    out = []
    for row in map(lambda i: inp + '-' + str(i), range(128)):
        out.append(knot_hash(row))
    return np.unpackbits(np.asanyarray(out), axis=-1)


grid = make_grid('jxqlasbh')

print(np.sum(grid))

def count_regions(grid):
    out = []
    while True:
        idxs = np.argwhere(grid == 1)
        if len(idxs) == 0:
            return out
        out.append(remove_region(grid, idxs[0]))

def neighbours(idx, grid):
    out = []
    if idx[0] > 0:
        out.append((idx[0] - 1, idx[1]))
    if idx[1] > 0:
        out.append((idx[0], idx[1] - 1))
    if idx[0] < grid.shape[0] - 1:
        out.append((idx[0] + 1, idx[1]))
    if idx[1] < grid.shape[1] - 1:
        out.append((idx[0], idx[1] + 1))
    return out

def remove_region(grid, idx):
    grid[tuple(idx)] = 0

    size = 1
    for n in neighbours(idx, grid):
        if grid[n]:
            size += remove_region(grid, n)
    return size

print(len(count_regions(grid.copy())))
