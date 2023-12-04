def get_lines(path):
    with open(path) as f:
        lines = f.readlines()
    return lines

def get_value(line: str):
    digits = [char for char in line if char in '0123456789']
    if len(digits) == 1:
        digits.append(digits[0])
    elif len(digits) > 2:
        digits = [digits[0], digits[-1]]
    val = ''.join(digits)
    return int(val)

def run_tests(tests):
    for i, (line, correct) in enumerate(tests.items()):
        val = get_value(line)
        try:
            assert val == correct
            print(f'[o] Test {i} Passed')
        except AssertionError:
            print(f'[x] Test {i} Failed: {line} --> {val}, [o] {correct}')

def run_final(lines):
    vals = [get_value(line) for line in lines]
    return sum(vals)

if __name__ == "__main__":
    tests = {
        '1abc2' : 12,
        'pqr3stu8vwx' : 38,
        'a1b2c3d4e5f' : 15,
        'treb7uchet' : 77
    }
    run_tests(tests)
    test_sum = run_final(tests.keys())
    print('Final test:', test_sum)
    input_01 = get_lines('inputs/input-01.txt')
    final_sum = run_final(input_01)
    print('Final value:', final_sum)

