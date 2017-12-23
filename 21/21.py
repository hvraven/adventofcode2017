#!/usr/bin/env python3

import numpy as np

start = np.array([[0,1,0], [0,0,1], [1,1,1]], dtype=bool)

def parse_matrix(s):
    lines = s.split('/')
    out = []
    for line in lines:
        out.append([x == '#' for x in line])
    return np.asarray(out)

def idx(block):
    bits = np.packbits(block, axis=None)
    if block.shape[0] == 3:
        return int(bits[...,0]) + int(bits[...,1]) * 2
    else:
        return int(bits) // 16

small = np.zeros((2**4, 3, 3), dtype=bool)
large = np.zeros((2**9, 4, 4), dtype=bool)
with open('input', 'r') as f:
    for line in f.readlines():
        frm, to = line.strip().split(' => ')
        frm = parse_matrix(frm)
        to = parse_matrix(to)
        if frm.shape[0] == 2:
            rules = small
        else:
            rules = large

        for i in range(4):
            block = np.rot90(frm, i)
            rules[idx(block)] = to
            block = np.flipud(block)
            rules[idx(block)] = to

def get(rules, block):
    return rules[idx(block)].squeeze()

def enhance(image):
    if image.shape[0] % 2 == 0:
        rules = small
        bs = 2
    else:
        rules = large
        bs = 3

    out = []
    for i in range(0, image.shape[0], bs):
        line = image[i:i+bs]
        outl = []
        for j in range(0, image.shape[1], bs):
            block = line[:,j:j+bs]
            nblock = get(rules, block) 
            outl.append(nblock)
        out.append(outl)
    return np.bmat(out)

image = start.copy()
for i in range(5):
    image = enhance(image)
    print(image.shape)
print(np.sum(image))
for i in range(13):
    image = enhance(image)
    print(image.shape)
print(np.sum(image))

