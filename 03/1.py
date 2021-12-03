from collections import defaultdict
one_counter = defaultdict(int) 
total = 0
with open('input.txt', 'r') as f:
    for line in f:
        total += 1
        bits = line.strip()
        for i, b in enumerate(bits):
            if b == '1':
                one_counter[i] += 1
    gamma = ''
    epsilon = ''
    for j in range(i+1):
        if one_counter[j] > total/2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    print(int(gamma, 2)*int(epsilon, 2))


