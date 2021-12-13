grid = []
valid_coords = set()
with open('input.txt', 'r') as f:
    for y, line in enumerate(f):
        row = []
        for x, number in enumerate(line.strip()):
            row.append(int(number))
            valid_coords.add((y, x))
        grid.append(row)
max_x, max_y = x+1, y+1
neighbours = lambda x, y: (
                (x+dx, y+dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] 
                if not(dx == dy == 0) and (x+dx, y+dy) in valid_coords
            )
i = 0
while True:
    flashed = set()
    to_flash_stack = set()
    for y, x in valid_coords:
        grid[y][x] += 1
        if grid[y][x] > 9:
            to_flash_stack.add((y, x))
    while to_flash_stack:
        y, x = to_flash_stack.pop()
        flashed.add((y, x))
        for x2, y2 in neighbours(x, y):
            grid[y2][x2] += 1
            if grid[y2][x2] > 9 and (y2, x2) not in flashed:
                to_flash_stack.add((y2, x2))
    i+=1
    if len(flashed) == max_x * max_y:
        break
    for y, x in flashed:
        grid[y][x] = 0

print(i)
      
