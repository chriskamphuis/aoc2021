easy_digits = {2: 1, 3: 7, 4: 4, 7: 8}
final = 0
with open('input.txt', 'r') as f:
    for line in f:
        numbers, display = line.strip().split(' | ')
        digits_to_letters = dict()
        to_solve = {n for n in numbers.split(' ')}
        solved = set()
        for d in to_solve: # Easy digits: 1, 4, 7, 8
            if len(d) in [2, 3, 4, 7]:
                digits_to_letters[easy_digits[len(d)]] = set(d) 
                solved |= {d}
        to_solve -= solved
        for d in to_solve: # Number 9
            if len(d) == 6 and digits_to_letters[4] <= set(d):
                digits_to_letters[9] = set(d)
                solved = {d}
        to_solve -= solved
        solved = set()
        for d in to_solve: # Number 0 and 6
            if len(d) == 6 and digits_to_letters[1] <= set(d):
                digits_to_letters[0] = set(d)
                solved |= {d}
            elif len(d) == 6:
                digits_to_letters[6] = set(d)
                solved |= {d}
        to_solve -= solved
        for d in to_solve: # Number 2
            if len(d) == 5 and not digits_to_letters[9] >= set(d):
                digits_to_letters[2] = set(d)
                solved = {d}
        to_solve -= solved
        for d in to_solve: # Number 3 and 5
            if digits_to_letters[1] <= set(d):
                digits_to_letters[3] = set(d)
            else:
                digits_to_letters[5] = set(d)
        score = 0
        for d in display.split(' '): 
            for digit, letters in digits_to_letters.items():
                if set(d) >= letters >= set(d):
                    if score:
                        score *= 10
                    score += digit
        final += score
print(final)


