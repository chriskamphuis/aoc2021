from collections import defaultdict

counts = defaultdict(int)
polymer = ''

with open('input.txt', 'r') as f:
    for c in f.readline().strip():
        polymer += c
        counts[c] += 1
    f.readline()
    instructions = {a:b for a, b in [line.strip().split(' -> ') for line in f]}

for _ in range(10):
    print(_)
    insert = ''.join([instructions[''.join(polymer[i:i+2])] for i in range(len(polymer)-1)])
    for i in insert:
        counts[i] += 1
    polymer = [a for b in zip(polymer, insert) for a in b] + [polymer[-1]]

print(max(counts.values()) - min(counts.values()))
