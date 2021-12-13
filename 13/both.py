coordinates = set()
instructions = []
lx, ly = 0, 0
with open('input.txt', 'r') as f:
    line = f.readline().strip()
    while line:
        x, y = line.split(',')
        coordinates.add((int(x), int(y)))
        if int(x) > lx:
            lx = int(x)
        if int(y) > ly:
            ly = int(y)
        line = f.readline().strip()
    for line in f: 
        axis, l = line.strip().split(' ')[-1].split('=')
        instructions.append((axis, int(l)))
for i, (axis, line) in enumerate(instructions):
    new_coordinates = set()
    if axis == 'x':
        lx //= 2
        for x, y in coordinates:
            if x > line:
                new_coordinates.add((line - (x - line), y))
            else:
                new_coordinates.add((x, y))

    else:
        ly //= 2
        for x, y in coordinates:
            if y > line:
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
