from collections import defaultdict

paths = defaultdict(set)
with open('input.txt', 'r') as f:
    for line in f:
        f, t = line.strip().split('-')
        paths[f].add(t)
        paths[t].add(f)

all_paths = set()
def sum_find_path(node, visited, vtwice, path=[]):
    path.append(node)
    if node == 'end':
        all_paths.add(''.join(path))
        return 1
    if node == 'start' and node in visited:
        return 0
    if node == 'start':
        visited |= {'start'}
    if vtwice:
        return sum([sum_find_path(n, visited | {node}, vtwice, [p for p in path]) for n in paths[node] if not(n.islower() and n in visited)])
    else:
        if node.islower() and not(node == 'start'):
            return (sum([sum_find_path(n, visited, True, [p for p in path]) for n in paths[node] if not(n.islower() and n in visited)]) + 
                    sum([sum_find_path(n, visited | {node}, vtwice, [p for p in path]) for n in paths[node] if not(n.islower() and n in visited)]))
        return sum([sum_find_path(n, visited | {node}, vtwice, [p for p in path]) for n in paths[node] if not(n.islower() and n in visited)])
 
sum_find_path('start', set(), False)
print(len(all_paths))
