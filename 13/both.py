coordinates = set()
instructions = []
lx, ly = 0, 0
with open('input.txt', 'r') as f:
    line = f.readline().strip()
    while line:
        x, y = line.split(',')
        coordinates.add((int(x), int(y)))
        line = f.readline().strip()
    for line in f: 
        axis, l = line.strip().split(' ')[-1].split('=')
        instructions.append((axis, int(l)))

for i, (axis, line) in enumerate(instructions):
    new_coordinates = set()
    for x, y in coordinates:
        if x > line and axis == 'x':
            new_coordinates.add((line - (x - line), y))
        elif y > line and axis == 'y':
            new_coordinates.add((x, line - (y - line)))
        else:
            new_coordinates.add((x, y))
    coordinates = new_coordinates
    if not i: 
        print(len(coordinates))

for row in range(int(ly+1)):
    for col in range(int(lx+1)):
        if (col, row) in coordinates:
            print('#', end='')
        else:
            print(' ', end='')
    print()
