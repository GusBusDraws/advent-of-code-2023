def get_lines(path):
    with open(path) as f:
        lines = f.readlines()
    return lines

def make_games_dict(lines):
    games = {}
    for line in lines:
        # Drop the newline character
        line = line[:-1]
        data_start = line.find(':')
        game_i = int(line[5 : data_start])
        games[game_i] = {
            'red' : [],
            'green' : [],
            'blue' : []
        }
        grabs = line[data_start + 2 :].split('; ')
        for grab in grabs:
            for color in grab.split(', '):
                games[game_i][color[color.find(' ')+1 :]].append(
                    int(color[0 : color.find(' ') ])
                )
    return games

def get_min_possible(game : dict):
    min_possible = {}
    for color in ['red', 'green', 'blue']:
        min_possible[color] = max(game[color])
    return min_possible

def run_tests(tests):
    correct_vals = [
        [4, 2, 6],
        [1, 3, 4],
        [20, 13, 6],
        [14, 3, 15],
        [6, 3, 2],
    ]
    games = make_games_dict(tests)
    for i, game in enumerate(games.values()):
        min_possible = get_min_possible(game)
        min_possible_list = list(min_possible.values())
        try:
            assert min_possible_list == correct_vals[i]
            print(f'[o] Passed: {game} --> {min_possible_list}')
        except AssertionError:
            print(
                f'[ ] Failed: {game} --> {min_possible_list},'
                f'[o] {correct_vals[i]}'
            )

def run_final(lines, test_val=None):
    games = make_games_dict(lines)
    min_possible_by_game = []
    for i, game in enumerate(games.values()):
        min_possible_by_game.append(get_min_possible(game))
    powers = [
        min_possible['red'] * min_possible['green'] * min_possible['blue']
        for min_possible in min_possible_by_game
    ]
    powers_sum = sum(powers)
    if test_val is not None:
        min_possible_abbrev = [
            list(min_possible.values()) for min_possible in min_possible_by_game
        ]
        try:
            assert run_final(lines) == test_val
            print(f'[o] Passed: {min_possible_abbrev} --> {powers_sum}')
        except AssertionError:
            print(
                f'[ ] Failed: {min_possible_abbrev} --> {powers_sum},'
                f'[o] {test_val}'
            )
    else:
        return powers_sum


if __name__ == "__main__":
    tests = [
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\n'
    ]
    run_tests(tests)
    run_final(tests, test_val=2286)
    input_02 = get_lines('inputs/input-02.txt')
    final_sum = run_final(input_02)
    print('Final value:', final_sum)

