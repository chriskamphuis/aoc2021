from collections import defaultdict

with open('input.txt', 'r') as f:
    numbers = [int(e) for e in f.readline().strip().split(',')]
    f.readline()
    r=0
    numbers_left_on_board = defaultdict(set)
    number_lboards_position = defaultdict(dict)
    number_to_board = defaultdict(set)
    boards_left = set()
    board_no = 0
    for line in f:
        l = line.strip()
        if not l:
            board_no+=1
            r=0
            continue
        c=0
        for number in l.split(' '):
            boards_left.add(board_no)
            if number.strip():
                n = int(number)
                numbers_left_on_board[board_no] |= {n}
                number_to_board[n] |= {board_no}
                number_lboards_position[n][board_no] = (r, c)
                c+=1
        r+=1
        c=0
number_board_col_count = defaultdict(lambda: defaultdict(int))
number_board_row_count = defaultdict(lambda: defaultdict(int))

done = set()
bre = False
for n in numbers:
    boards = number_to_board[n]
    for b in boards:
        if b in done:
            continue
        numbers_left_on_board[b].remove(n)
        row, col = number_lboards_position[n][b]
        number_board_col_count[b][col] += 1
        number_board_row_count[b][row] += 1
        if number_board_col_count[b][col] == 5 or number_board_row_count[b][row] == 5:
            boards_left.remove(b)
            done.add(b)
            if len(boards_left) == 0:
                print(n*sum(numbers_left_on_board[b]))
