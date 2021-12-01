lines = [int(d.strip()) for d in open('input.txt').readlines()]
count = 0
for i in range(1, len(lines)):
    if lines[i] > lines[i-1]:
        count+=1
print(count)

