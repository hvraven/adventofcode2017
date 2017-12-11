#!/usr/bin/env python3

from toolz.itertoolz import accumulate, frequencies

with open('input', 'r') as f:
    inp = f.readline().strip().split(',')

def total_movement(counts):
    straight = counts['nw'] - counts['se']
    left = counts['sw'] - counts['ne']
    right = counts['n'] - counts['s']
    straight += left
    right -= left

    return abs(straight + right)

print(total_movement(frequencies(inp)))

counts = {dir: 0 for dir in ['n', 'nw', 'ne', 's', 'sw', 'se']}
def single_count(counts, direction):
    counts[direction] += 1
    return counts.copy()

print(max(map(total_movement, accumulate(single_count, inp, counts))))
