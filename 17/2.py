(xmin, xmax), (ymin, ymax) = [
            [int(a) for a in e.split('=')[-1].split('..')] 
            for e in open('input.txt', 'r').read().strip().replace(',', '').split(' ')[-2:]
        ]

def trajectory(dx, dy, xmax, ymax):
    x, y = 0, 0
    while x < xmax and y > ymin:
        x += dx
        y += dy
        yield x, y
        if dx > 0: dx -= 1
        if dx < 0: dx += 1
        dy -= 1

any_in_target_area = lambda t, xmin, xmax, ymin, ymax: any([xmin<=x<=xmax and ymin<=y<=ymax for x, y in t])

dx, dy = xmax, (xmax//2)+1
count = 0
while True:
    t = trajectory(dx, dy, xmax, ymax)
    if any_in_target_area(t, xmin, xmax, ymin, ymax): count += 1
    dx -= 1
    if dx == 0:
        dx = xmax
        dy -= 1
    if dy == ymin-1: break
print(count)

