#!/usr/bin/env python3

import sys

valid1 = 0
valid2 = 0
for line in sys.stdin.readlines():
    words = line.strip().split(' ')
    if len(words) == len(set(words)):
        valid1 += 1
    sw = list(map(lambda x: ''.join(sorted(x)), words))
    if len(sw) == len(set(sw)):
        valid2 += 1

print(valid1)
print(valid2)
