c=0
with open('input.txt', 'r') as f:
    for line in f:
        numbers, display = line.strip().split(' | ')
        for d in display.split(' '):
            if len(d) in [2, 3, 4, 7]:
                c+=1
print(c)
