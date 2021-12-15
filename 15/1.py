import heapq

grid = []
costs = []
with open('input.txt', 'r') as f:
    for line in f:
        grid.append([int(c) for c in line.strip()])
        costs.append([float('inf') for _ in range(len(line.strip()))])
goal = (len(grid[0])-1, len(grid)-1) # goal (x, y)
visited = set()
to_visit = []
heapq.heappush(to_visit, (grid[0][0], (0, 0)))

neighbours = lambda x, y: [(a,b) for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] if 0 <= a <= goal[1] and 0 <= b <= goal[0]]

while goal not in visited:
    cost, (y, x) = heapq.heappop(to_visit)
    if (y,x) in visited:
        continue
    costs[y][x] = cost
    for (ny, nx) in neighbours(y, x):
        if (ny, nx) not in visited:
            heapq.heappush(to_visit, (costs[y][x]+grid[ny][nx], (ny, nx)))
    visited.add((y, x))
print(costs[goal[0]][goal[1]] - costs[0][0])
     
