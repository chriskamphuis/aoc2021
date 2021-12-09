import heapq

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

lowpoints = []
for y in range(1, len(data)-1):
    for x in range(1, len(data[0])-1):
        if (data[y][x] < data[y-1][x] and 
            data[y][x] < data[y+1][x] and
            data[y][x] < data[y][x-1] and 
            data[y][x] < data[y][x+1]):
            lowpoints.append((y, x))

def neighbours(x, y):
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

heap = [0, 0, 0]

visited = [[False for _ in range(len(data))] for _ in range(len(data[1]))]
for (y, x) in lowpoints:
    basin_size = 0
    to_visit = [(y, x)]
    visited[y][x] = True
    while to_visit:
        k,j = to_visit.pop()
        basin_size += 1
        for (b, a) in neighbours(k, j):
            if visited[b][a] or data[b][a] == 9:
                continue
            to_visit.append((b, a))
            visited[b][a] = True
    heapq.heappushpop(heap, basin_size) 
print(heap[0] * heap[1] * heap[2])
