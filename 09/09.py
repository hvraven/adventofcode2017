#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10000)

with open('input', 'r') as f:
    inp = f.readline().strip()

def inc(x, y, tpl):
    return x + tpl[0], y + tpl[1]

def score(inp, ls = 1):
    if not inp:
        return 0, 0
    c = inp[0]
    if c == '{':
        return inc(ls, 0, score(inp[1:], ls + 1))
    elif c == '}':
        return score(inp[1:], ls - 1)
    elif c == ',':
        return score(inp[1:], ls)
    elif c == '<':
        return comment(inp[1:], ls)
    else:
        raise Exception(c)

def comment(inp, ls):
    for i, c in enumerate(inp):
        if c == '!':
            return inc(0, i, comment(inp[i+2:], ls))
        elif c == '>':
            return inc(0, i, score(inp[i+1:], ls))

print(score(inp))

