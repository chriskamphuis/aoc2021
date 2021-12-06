states = [0 for _ in range(9)]
for e in open('input.txt', 'r').read().strip().split(','):
    states[int(e)] += 1
for i in range(256):
    states[(7+i)%9] += states[i%9] 
print(sum(states))
