#!/usr/bin/env python3

import numpy as np

inp = np.genfromtxt('input', delimiter=',', dtype=np.int)

def run_sequence(seq, rounds=1):
    clist = np.arange(0, 256, dtype=np.int)
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

clist = run_sequence(inp)
print(clist[0] * clist[1])

with open('input', 'r') as f:
    inp = np.fromstring(f.readline().strip(), dtype=np.uint8)
    inp = np.concatenate((inp, [17, 31, 73, 47, 23]))

sparse_hash = run_sequence(inp, 64)
dense_hash = np.bitwise_xor.reduce(sparse_hash.reshape((16,16)), axis=1)

print(''.join(map(lambda x: format(x, '02x'), dense_hash)))
