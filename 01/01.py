#!/usr/bin/env python3

import numpy as np
import sys

def part1(digits):
    return np.sum(digits[digits == np.roll(digits, -1)])

def part2(digits):
    return np.sum(digits[digits == np.roll(digits, int(len(digits)/-2))])

for line in sys.stdin.readlines():
    digits = np.fromiter(line.strip(), dtype=np.uint8)
    print(part1(digits))
    print(part2(digits))

