#!/usr/bin/env python3

def set(data, reg, val):
    data[reg] = get_value(data, val)

def sub(data, a, b):
    data[a] = data.get(a, 0) - get_value(data, b)

def mul(data, a, b):
    data[a] = data.get(a, 0) * get_value(data, b)

def jnz(data, a, b):
    if get_value(data, a) != 0:
        data['instr'] += get_value(data, b) - 1

def get_value(data, a):
    if isinstance(a, str):
        return data.get(a, 0)
    else:
        return int(a)

def parse(line):
    split = line.split(' ')
    cmd = globals()[split[0]]
    def try_int(x):
        try:
            return int(x)
        except:
            return x
    args = tuple(map(try_int, split[1:]))
    return cmd, args

with open('input', 'r') as f:
    inp = f.read().strip().split('\n')

cmds = list(map(parse, inp))

def execute(cmds):
    data = dict(instr=0)
    count = 0
    while 0 <= data['instr'] < len(cmds):
        cmd, args = cmds[data['instr']]
        cmd(data, *args)
        data['instr'] += 1
        if cmd == mul:
            count += 1
    return count

print(execute(cmds))
