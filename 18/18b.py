#!/usr/bin/env python3

def set(data, reg, val):
    data[reg] = get_value(data, val)

def snd(data, val):
    data['count'] += 1
    data['out'].append(get_value(data, val))

def add(data, a, b):
    data[a] = data.get(a, 0) + get_value(data, b)

def mul(data, a, b):
    data[a] = data.get(a, 0) * get_value(data, b)

def mod(data, a, b):
    data[a] = data.get(a, 0) % get_value(data, b)

def rcv(data, a):
    data[a] = data['in'].pop(0)

def jgz(data, a, b):
    if get_value(data, a) > 0:
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

def execute_parallel(data, cmds):
    data['out'] = []
    data['count'] = 0
    while 0 <= data['instr'] < len(cmds):
        cmd, args = cmds[data['instr']]
        if cmd == rcv and len(data['in']) == 0:
            yield data['out']
            data['out'] = []
        cmd(data, *args)
        data['instr'] += 1

def dual_execute(cmds):
    data0 = {'instr': 0, 'p': 0, 'in': []}
    data1 = {'instr': 0, 'p': 1, 'in': []}

    gen0 = execute_parallel(data0, cmds)
    gen1 = execute_parallel(data1, cmds)

    data1['in'] = next(gen0)
    while True:
        data0['in'] += next(gen1)
        if len(data0['in']) == 0:
            break
        data1['in'] += next(gen0)
        if len(data1['in']) == 0:
            break
    return data0, data1

print(dual_execute(cmds)[1]['count'])
