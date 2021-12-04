from collections import defaultdict

with open('input.txt', 'r') as f:
    numbers = [int(e) for e in f.readline().strip().split(',')]
    f.readline()
    i=0
    r=0
    numbers_left_on_board = defaultdict(set)
    number_lboards_position = defaultdict(dict)
    number_to_board = defaultdict(set)
    for line in f:
        l = line.strip()
        if not l:
            i+=1
            r=0
            continue
        c=0
        for number in l.split(' '):
            if number.strip():
                n = int(number)
                numbers_left_on_board[i] |= {n}
                number_to_board[n] |= {i}
                number_lboards_position[n][i] = (r, c)
                c+=1
        r+=1
        c=0
number_board_col_count = defaultdict(lambda: defaultdict(int))
number_board_row_count = defaultdict(lambda: defaultdict(int))

bre = False
for n in numbers:
    boards = number_to_board[n]
    for b in boards:
        numbers_left_on_board[b].remove(n)
        col, row = number_lboards_position[n][b]
        number_board_col_count[b][col] += 1
        number_board_row_count[b][row] += 1
        if number_board_col_count[b][col] == 5 or number_board_row_count[b][row] == 5:
            bre = True
            print(n*sum(numbers_left_on_board[b]))
            break
    if bre:
        break
