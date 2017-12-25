#!/usr/bin/env python3

import numpy as np 

class Dancers(object):
    def __init__(self):
        self.dancers = np.arange(16, dtype=np.uint8)
        self.positions = np.arange(16, dtype=np.uint8)

    def spin(self, n):
        self.dancers = np.roll(self.dancers, n)
        self.positions += n
        self.positions %= 16

    def exchange(self, i, j):
        self.dancers[i], self.dancers[j] = self.dancers[j], self.dancers[i]
        ix = self.dancers[i]
        iy = self.dancers[j]
        self.positions[ix], self.positions[iy] = self.positions[iy], self.positions[ix]

    def partner(self, ix, iy):
        self.positions[ix], self.positions[iy] = self.positions[iy], self.positions[ix]
        i = self.positions[ix]
        j = self.positions[iy]
        self.dancers[i], self.dancers[j] = self.dancers[j], self.dancers[i]

    def __str__(self):
        return ''.join(list(map(lambda x: chr(x + ord('a')), list(self.dancers))))


def dance(cmds, dancers=Dancers()):
    for fun, args in cmds:
        if fun == 's':
            dancers.spin(*args)
        elif fun == 'x':
            dancers.exchange(*args)
        else:
            dancers.partner(*args)
    return dancers


inp = np.genfromtxt('input', delimiter=',', dtype=str)

cmds = []
for token in inp:
    if token[0] == 's':
        cmds.append(('s', (int(token[1:]),)))
    if token[0] == 'x':
        ints = token[1:].split('/')
        cmds.append(('x', (int(ints[0]), int(ints[1]))))
    if token[0] == 'p':
        toks = token[1:].split('/')
        cmds.append(('p', (int(ord(toks[0]) - ord('a')),
            int(ord(toks[1]) - ord('a')))))

i = 1
seen = {}
dancers = Dancers()
while True:
    dancers = dance(cmds, dancers)
    if str(dancers) in seen.keys():
        break
    seen[str(dancers)] = i
    i += 1

for k, v in seen.items():
    if v == 1:
        print(k)

n = 1000000000 % len(list(seen.values()))
for k, v in seen.items():
    if v == n:
        print(k)
