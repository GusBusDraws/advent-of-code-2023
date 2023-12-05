def get_lines(path):
    with open(path) as f:
        # Drop the newline character
        lines = [line[:-1] for line in f.readlines()]
    return lines

def find_potential_parts(line):
    splits = line.split('.')
    splits = [split for split in splits if split != '']
    split_dict = {}
    for split in splits:
        start_i = line.find(split)
        split_idcs = list(range(start_i, start_i + len(split)))
        split_dict[split] = split_idcs
    print(split_dict)

def find_parts(lines):
    parts = []
    for line_i, line in enumerate(lines):
        chars = {i: char for i, char in enumerate(line) if char in '0123456789'}
        if line_i > 0:
            prev_line_symbol_idcs = check_for_symbols(lines, line_i - 1)
        this_line_symbol_idcs = check_for_symbols(lines, line_i)
        if line_i < len(lines):
            next_line_symbol_idcs = check_for_symbols(lines, line_i + 1)
        for char_i, char in chars.items():
            if char_i > 0:
                pass

def check_for_symbols(lines, line_i):
    pass

def check_for_neighboring_symbols(lines, line_i, char_idcs):
    pass

def run_tests(tests):
    for i, (line, correct) in enumerate(tests.items()):
        parts = find_parts(line)
        try:
            assert parts == correct
            print(f'[o] Passed')
        except AssertionError:
            print(f'[x] Failed: {line} --> {parts}, [o] {correct}')

def run_final(lines, test_val=None):
    parts_sum = sum([sum(find_parts(line)) for line in lines])
    if test_val is not None:
        try:
            assert run_final(lines) == test_val
            print(f'[o] Passed')
        except AssertionError:
            print(f'[ ] Failed: {parts_sum}, [o] {test_val}')
    else:
        return parts_sum


if __name__ == "__main__":
    tests = {
        '467..114..\n' : [467],
        '...*......\n' : [],
        '..35..633.\n' : [35, 633],
        '......#...\n' : [],
        '617*......\n' : [617],
        '.....+.58.\n' : [],
        '..592.....\n' : [592],
        '......755.\n' : [755],
        '...$.*....\n' : [],
        '.664.598..\n' : [664, 598],
    }
    line = list(tests.keys())[0][:-1]
    print(line)
    find_potential_parts(line)
    # run_tests(tests)
    # run_final(tests, test_val=4361)
    # input_03 = get_lines('inputs/input-03.txt')
    # final_sum = run_final(input_03)
    # print('Final value:', final_sum)

