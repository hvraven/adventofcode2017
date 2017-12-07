#!/usr/bin/env python3

import attr
import operator
import re

@attr.s
class TreeNode(object):
    own_weight = attr.ib(convert=int)
    above = attr.ib(default=[])

    


with open('input', 'r') as f:
    reg = re.compile(r'(\w*) \((\d*)\)( -> [a-z, ]*)?')
    tree = {}
    for line in f.readlines():
        match = reg.match(line)
        if match.group(3):
            above = match.group(3)[4:].split(', ')
        else:
            above = []
        out = TreeNode(match.group(2), above)
        tree[match.group(1)] =  out

all_names = set(tree.keys())
all_above = set(reduce(operator.add, map(lambda x: x.above, tree.values()), []))

start_node = list(all_names - all_above)[0]
print(start_node)

def build_tree(itree, start):
    return TreeNode(itree[start].own_weight,
                    list(map(lambda x: build_tree(itree, x),
                             itree[start].above)))

real_tree = build_tree(tree, start_node)

def check_weights(node):
    if not node.above:
        return node.own_weight

    weights = list(map(check_weights, node.above))
    if not all(weights[0] == w for w in weights):
        print(weights)
        print(list(map(lambda n: n.own_weight, node.above)))
    return reduce(operator.add, weights, node.own_weight)

check_weights(real_tree)
