data = []
with open('input.txt', 'r') as f:
    line = f.readline().strip()
    rowlen = len(line)
    ninerow = [9 for _ in range(rowlen+2)]
    data.append(ninerow) 
    while line:
        row = [9]
        for c in line.strip():
            row.append(int(c))
        row.append(9)
        data.append(row)
        line = f.readline().strip()
    data.append(ninerow)

score = 0
for y in range(1, len(data)-1):
    for x in range(1, len(data[0])-1):
        if (data[y][x] < data[y-1][x] and 
            data[y][x] < data[y+1][x] and
            data[y][x] < data[y][x-1] and 
            data[y][x] < data[y][x+1]):
            score += data[y][x] + 1
print(score)
