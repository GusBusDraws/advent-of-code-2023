def get_lines(path):
    with open(path) as f:
        lines = f.readlines()
    return lines

def find_all(full_str, search):
    found_idcs = []
    loop = True
    start = 0
    while loop:
        start = full_str.find(search, start)
        if start == -1: loop = False
        if start != -1: found_idcs.append(start)
        start += len(search)
    return found_idcs

def find_words(line : str, found_digits_by_idx : dict):
    digit_map = {
        'zero'  : 0,
        'one'   : 1,
        'two'   : 2,
        'three' : 3,
        'four'  : 4,
        'five'  : 5,
        'six'   : 6,
        'seven' : 7,
        'eight' : 8,
        'nine'  : 9
    }
    for word in digit_map.keys():
        if word in line:
            idcs = find_all(line, word)
            # print(f'{word} found in {line} at {idcs}')
            for i in idcs:
                found_digits_by_idx[i] = digit_map[word]
    return found_digits_by_idx

def find_digits(line : str):
    found_digits_by_idx = {}
    found_digits_by_idx = {
        i : char for i, char in enumerate(line) if char in '0123456789'
    }
    return found_digits_by_idx

def process_found_digits(found_digits_by_idx : dict):
    found_digits_by_idx = dict(sorted(found_digits_by_idx.items()))
    digits = [str(digit) for digit in found_digits_by_idx.values()]
    val = ''.join(digits)
    if len(val) == 1:
        val += val
    elif len(val) > 2:
        val = val[0] + val[-1]
    return int(val)

def run_tests(tests):
    for i, (line, correct) in enumerate(tests.items()):
        found_digits_by_idx = find_digits(line)
        found_digits_by_idx = find_words(line, found_digits_by_idx)
        val = process_found_digits(found_digits_by_idx)
        try:
            assert val == correct
            print(f'[o] Passed: {line} --> {val}')
        except AssertionError:
            print(f'[ ] Failed: {line} --> {val}, [o] {correct}')

def run_final(lines):
    vals = []
    for line in lines:
        found_digits_by_idx = find_digits(line)
        found_digits_by_idx = find_words(line, found_digits_by_idx)
        vals.append(process_found_digits(found_digits_by_idx))
    return sum(vals)

if __name__ == "__main__":
    tests = {
        'two1nine'         : 29,
        'eightwothree'     : 83,
        'abcone2threexyz'  : 13,
        'xtwone3four'      : 24,
        '4nineeightseven2' : 42,
        'zoneight234'      : 14,
        '7pqrstsixteen'    : 76
    }
    other_cases = {
        'one8one' : 11
    }
    run_tests(tests)
    test_sum = run_final(tests.keys())
    print('Final test:', test_sum)
    run_tests(other_cases)
    input_01 = get_lines('inputs/input-01.txt')
    final_sum = run_final(input_01)
    print('Final value:', final_sum)

