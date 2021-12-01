lines = [int(d.strip()) for d in open('input.txt').readlines()]
count = 0
for i in range(1, len(lines)-2):
    if sum(lines[i:i+3]) > sum(lines[i-1:i+2]):
        count+=1
print(count)

