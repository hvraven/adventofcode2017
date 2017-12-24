#!/usr/bin/env python3

import attr
import numpy as np
from itertools import groupby

with open('input', 'r') as f:
    out = []
    for line in f.readlines():
        l = []
        for vec in line.strip().split(', '):
            name, vals = vec.replace('>', '').split('=<')
            l.append(list(map(int, vals.split(','))))
        out.append(l)
    inp = np.asarray(out)

print(np.argmin(np.sum(np.abs(inp[:,2]), axis=-1)))

def possible_collisions(particles):
    cols = []
    for p1 in range(particles.shape[0]):
        for p2 in range(p1+1, particles.shape[0]):
            dp = particles[p1,:,0] - particles[p2,:,0]
            n = []
            if dp[2] == 0:
                if dp[1] == 0:
                    continue
                n = [-dp[0] / dp[1]]
            else:
                b = dp[1] + dp[2] / 2
                sq = np.sqrt(b**2 - 2*dp[2]*dp[0])
                n = [(-b + sq) / dp[2], (-b - sq) / dp[2]]
            dp = particles[p1] - particles[p2]
            for pn in n:
                if not np.isfinite(pn) or not np.isclose(int(pn), pn):
                    continue
                pn = int(pn)
                if np.all(np.isclose(pn*(pn+1)/2 * dp[2] + pn * dp[1] + dp[0], 0)):
                    print((p1, p2, pn))
                    cols.append((p1, p2, pn))
    return cols

def collisions(inp):
    existing = np.ones(inp.shape[0], dtype=bool)
    possibles = np.asarray(possible_collisions(inp))
    possibles = possibles[np.argsort(possibles.T[2])]
    for group, elements in groupby(possibles, lambda x: x[2]):
        cols = []
        for e in elements:
            if existing[e[0]] and existing[e[1]]:
                cols.append(e)
        for c in cols:
            existing[c[0]] = False
            existing[c[1]] = False
    
    return np.sum(existing)

print(collisions(inp))
