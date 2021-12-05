from collections import defaultdict
location_store = defaultdict(int)
final_locations = set()

def print_coordinates(co):
    for x in range(10):
        for y in range(10):
            if co[(x, y)] > 0:
                print(co[(x, y)], end='')
            else:
                print('.', end='') 
        print()

with open('input.txt', 'r') as f:
    for line in f:
        coords = line.strip().split(' -> ')
        from_c, to_c = [[int(e) for e in c.split(',')] for c in coords]
        if from_c[0] != to_c[0] and from_c[1] != to_c[1]:
            continue
        change_x = True if from_c[0] != to_c[0] else False
        if change_x:
            f, t = from_c[0], to_c[0]
            if f > t:
                f, t = t, f
            for c in range(f, t+1):
                location_store[(c, from_c[1])] += 1
                if location_store[(c, from_c[1])] == 2:
                    final_locations.add((c, from_c[1]))
        else:
            f, t = from_c[1], to_c[1]
            if f > t:
                f, t = t, f
            for c in range(f, t+1):
                location_store[(from_c[0], c)] += 1
                if location_store[(from_c[0], c)] == 2:
                    final_locations.add((from_c[0], c))
print(len(final_locations))
