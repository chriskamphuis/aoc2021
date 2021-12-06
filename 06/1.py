from collections import defaultdict

states = defaultdict(int)
for e in open('input.txt', 'r').read().strip().split(','):
    states[int(e)] += 1

for _ in range(80):
    new_states = defaultdict(int)
    new_states[8] = states[0]
    new_states[6] = states[0]
    for i in range(1, 9):
        new_states[i-1] += states[i]
    states = new_states
print(sum([v for k,v in states.items()]))
