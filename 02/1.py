depth, position = 0, 0
with open('input.txt', 'r') as f:
    for line in f:
        instruction, value = line.strip().split(' ')
        value = int(value)
        if instruction == 'forward':
            position += value
        elif instruction == 'down':
            depth += value
        else:
            depth -= value
print(depth * position)
