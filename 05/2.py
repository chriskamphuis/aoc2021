from collections import defaultdict
location_store = defaultdict(int)
final_locations = set()

with open('input.txt', 'r') as f:
    for line in f:
        coords = line.strip().split(' -> ')
        from_c, to_c = [[int(e) for e in c.split(',')] for c in coords]
        if from_c[0] != to_c[0] and from_c[1] != to_c[1]:
            for c1, c2 in zip(range(from_c[0], to_c[0] + int((to_c[0]-from_c[0])/abs(to_c[0]-from_c[0])), int((to_c[0]-from_c[0])/abs(to_c[0]-from_c[0]))), 
                              range(from_c[1], to_c[1] + int((to_c[1]-from_c[1])/abs(to_c[1]-from_c[1])), int((to_c[1]-from_c[1])/abs(to_c[1]-from_c[1])))):
                location_store[(c1, c2)] += 1
                if location_store[(c1, c2)] == 2:
                    final_locations.add((c1, c2))
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
