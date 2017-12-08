#!/usr/bin/env python3

import attr
import operator
from collections import defaultdict
from enum import Enum
from itertools import accumulate
from functools import reduce

class Ops(Enum):
    inc = 1
    dec = -1

class Conds(Enum):
    g = operator.gt
    l = operator.lt
    ge = operator.ge
    le = operator.le
    ee = operator.eq
    ne = operator.ne

def cond_parser(inp):
    translation = {'>': 'g', '<': 'l', '=': 'e', '!': 'n'}
    return Conds[''.join(map(translation.__getitem__, inp))]

@attr.s
class Instr(object):
    reg = attr.ib()
    op = attr.ib(convert=Ops.__getitem__)
    val = attr.ib(convert=int)
    creg = attr.ib()
    cond = attr.ib(convert=cond_parser)
    cval = attr.ib(convert=int)


def parse_input():
    with open('input', 'r') as f:
        out = []
        for line in f.readlines():
            words = line.strip().split(' ')
            instr = Instr(*(words[:3] +  words[4:]))
            out.append(instr)
        return out

def run_instruction(state, instr):
    if instr.cond.value(state[instr.creg], instr.cval):
        state[instr.reg] += instr.op.value * instr.val
    return state.copy()

instrs = parse_input()
final = reduce(run_instruction, instrs, defaultdict(int))
print(max(final.values()))
intermediates = list(accumulate((defaultdict(int), *instrs), run_instruction))
print(max(list(map(lambda x: max(x.values()), intermediates))))
