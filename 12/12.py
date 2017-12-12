#!/usr/bin/env python3

graph = {}
with open('input', 'r') as f:
    for l in f.readlines():
        node, neighbours = l.strip().split(' <-> ')
        graph[int(node)] = set(map(int, neighbours.split(', ')))

def calc_subgraph(tree, node, seen = set()):
    seen.add(node)
    map(lambda n: calc_subgraph(tree, n, seen), tree[node] - seen)
    return seen

print(len(calc_subgraph(graph, 0, set())))

def count_groups(tree):
    groups = 0
    nodes = set(tree.keys())
    while nodes:
        groups += 1
        nodes -= calc_subgraph(tree, nodes.pop())
    return groups

print(count_groups(graph))
