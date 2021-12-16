from math import prod

def char_stream():
    with open('input.txt', 'r') as f:
        while c := f.read(1).strip():
            yield c

bits = (b for g in  ('0000'[:4-len(g[2:])]+g[2:] for g in (bin(int(c, 16)) for c in char_stream())) for b in g)

def process_packet(bits):
    version = int(''.join(next(bits) for _ in range(3)), 2)
    typeid = int(''.join(next(bits) for _ in range(3)), 2)
    if typeid == 4: # literal
        literal = ''
        while c := next(bits):
            literal += ''.join(next(bits) for _ in range(4))
            if c == '0': break
        return int(literal, 2)
    operator =  int(next(bits), 2)
    values = []
    if operator == 0:
        len_sub_packets = int(''.join(next(bits) for _ in range(15)), 2)
        subpackets = (next(bits) for b in range(len_sub_packets))
        while True: 
            try:
                values.append(process_packet(subpackets))
            except RuntimeError:
                break
    else:
        values = [process_packet(bits) for _ in range(int(''.join(next(bits) for _ in range(11)), 2))]
    
    if typeid == 0: return sum(values)
    if typeid == 1: return prod(values)
    if typeid == 2: return min(values)
    if typeid == 3: return max(values)
    if typeid == 5: return int(values[0] > values[1])
    if typeid == 6: return int(values[0] < values[1])
    if typeid == 7: return int(values[0] == values[1])

print(process_packet(bits))
