from collections import defaultdict

polymer = ''
duo = defaultdict(int)

with open('input.txt', 'r') as f:
    polymer = f.readline().strip()
    f.readline()
    instructions = {a:b for a, b in [line.strip().split(' -> ') for line in f]}

first, last = polymer[0], polymer[-1]

for i in range(len(polymer)-1):
    duo[''.join(polymer[i:i+2])] += 1

for _ in range(40):
    new_duo = defaultdict(int)
    for key, count in duo.items():
        new_letter = instructions[key]
        new_duo[key[0] + new_letter] += count
        new_duo[new_letter + key[1]] += count
    duo = new_duo

count = defaultdict(int)
for key, value in duo.items():
    for letter in key:
        count[letter] += value
count[first] +=1
count[last] += 1
print(int(max(count.values())/2 - min(count.values())/2))
