# Tree for storing info
class Node:
    def __init__(self, one_child=None, zero_child=None, one_count=0, zero_count=0):
        self.one_child = one_child
        self.zero_child = zero_child
        self.one_count = one_count
        self.zero_count = zero_count

# Load the data in the tree
with open('input.txt', 'r') as f:
    root = Node()
    n = root
    for line in f:
        bits = line.strip()
        for i, b in enumerate(bits):
            if b == '1':
                n.one_count += 1
                if n.one_child is None:
                    n.one_child = Node()
                n = n.one_child 
            else:
                n.zero_count += 1
                if n.zero_child is None:
                    n.zero_child = Node()
                n = n.zero_child 
        n = root

# Oxygen value
o = root
oxygen = ''
for _ in range(i+1):
    if o.one_count >= o.zero_count:
        oxygen += '1'
        o = o.one_child
    else:
        oxygen += '0'
        o = o.zero_child
    
# CO2 scrub value
c = root
co2 = ''
for _ in range(i+1):
    if c.one_count < c.zero_count and c.one_count > 0 or c.zero_count == 0:
        co2 += '1'
        c = c.one_child
    else:
        co2 += '0'
        c = c.zero_child
print(int(oxygen, 2) * int(co2, 2))
