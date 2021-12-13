from collections import defaultdict

paths = defaultdict(set)
with open('input.txt', 'r') as f:
    for line in f:
        f, t = line.strip().split('-')
        paths[f].add(t)
        paths[t].add(f)

def sum_find_path(node, visited):
    if node == 'end':
        return 1
    return sum([sum_find_path(n, visited | {node} ) for n in paths[node] if not(n.islower() and n in visited)])

print(sum_find_path('start', set()))
