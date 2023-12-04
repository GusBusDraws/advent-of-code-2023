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
        #print(game)
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

def check_conditions(games : dict, conditions : dict):
    possible_games = []
    for game_i, details in games.items():
        if (
            (conditions['red'] >= max(details['red']))
            and (conditions['green'] >= max(details['green']))
            and (conditions['blue'] >= max(details['blue']))
        ):
            possible_games.append(game_i)
    return possible_games

def run_tests(tests, conditions, correct_games):
    games = make_games_dict(tests)
    possible_games = check_conditions(games, conditions)
    try:
        assert possible_games == correct_games
        print(f'[o] Passed: {possible_games}')
    except AssertionError:
        print(f'[ ] Failed: {possible_games}, [o] {correct_games}')

def run_final(lines):
    games = make_games_dict(lines)
    possible_games = check_conditions(games, conditions)
    return sum(possible_games)

if __name__ == "__main__":
    tests = [
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\n'
    ]
    conditions = {
        'red' : 12,
        'green' : 13,
        'blue' : 14
    }
    correct_games = [1, 2, 5]
    run_tests(tests, conditions, correct_games)
    test_sum = run_final(tests)
    print('Final test:', test_sum)
    input_02 = get_lines('inputs/input-02.txt')
    final_sum = run_final(input_02)
    print('Final value:', final_sum)

