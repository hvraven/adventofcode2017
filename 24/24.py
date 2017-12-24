#!/usr/bin/env python3

import numpy as np

inp = np.sort(np.genfromtxt('input', delimiter='/', dtype=int))
inp = inp[np.argsort(inp.T[0])]

def matching_idx(l, n):
    return np.nonzero(np.logical_or(l.T[0] == n, l.T[1] == n))

def strongest(l, current):
    matches = [0]
    idxs = matching_idx(l, current)[0]
    for idx in idxs:
        if l[idx][0] == current:
            nv = l[idx][1]
        else:
            nv = l[idx][0]
        n = np.delete(l, [idx], axis=0)
        matches.append(np.sum(l[idx]) + strongest(n, nv))

    return np.max(matches)

def longest(l, current):
    matches = [(0, 0)]
    idxs = matching_idx(l, current)[0]
    for idx in idxs:
        if l[idx][0] == current:
            nv = l[idx][1]
        else:
            nv = l[idx][0]
        n = np.delete(l, [idx], axis=0)
        length, strenghts = longest(n, nv)
        matches.append((1 + length, np.sum(l[idx]) + strenghts))

    matches = np.asarray(matches)
    longs = np.max(matches.T[0])
    return longs, np.max(matches.T[1][matches.T[0] == longs])

print(strongest(inp, 0))

print(longest(inp, 0)[1])




