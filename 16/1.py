def char_stream():
    with open('input.txt', 'r') as f:
        while c := f.read(1).strip():
            yield c

bits = (b for g in  ('0000'[:4-len(g[2:])]+g[2:] for g in (bin(int(c, 16)) for c in char_stream())) for b in g)
version_number_sum = 0

def process_packet(bits):
    version = int(''.join(next(bits) for _ in range(3)), 2)
    global version_number_sum
    version_number_sum += version
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
        return values
    else:
        no_packages = int(''.join(next(bits) for _ in range(11)), 2)
        for _ in range(no_packages):
            values.append(process_packet(bits))
        return values
    
process_packet(bits)
print(version_number_sum)
