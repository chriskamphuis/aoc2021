from statistics import median

chunks = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
openings = {'(', '[', '{', '<'}
illegals = {')': 0, ']': 0, '}': 0, '>': 0}
auto = {')': 1, ']': 2, '}': 3, '>': 4}
p2 = []

for line in open('input.txt'):
    stack = []
    p1 = False
    for c in line.strip():
        if c in openings:
            stack.append(c)
            continue
        if chunks[stack.pop()] == c:
            continue
        else:
            illegals[c] += 1
            p1 = True
            break
    if p1:
        continue
    score = 0
    while(len(stack) > 0):
        score *= 5
        score += auto[chunks[stack.pop()]]
    p2.append(score) 

print(sum([illegals[close]*scores[close] for close in [chunks[o] for o in openings]]))
print(int(median(p2)))
