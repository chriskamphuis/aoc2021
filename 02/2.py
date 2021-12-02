depth, position, aim = 0, 0, 0
with open('input.txt', 'r') as f:
    for line in f:
        instruction, value = line.strip().split(' ')
        value = int(value)
        if instruction == 'forward':
            position += value
            depth += aim * value
        elif instruction == 'down':
            aim += value
        else:
            aim -= value
print(depth * position)
