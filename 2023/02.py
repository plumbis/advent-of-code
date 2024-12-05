
def process_games():

    f = open("inputs/02.txt", "r", encoding="utf-8")

    games = {}
    # Game 1: 3 green, 1 blue, 3 red; 3 blue, 1 green, 3 red; 2 red, 12 green, 7 blue; 1 red, 4 blue, 5 green; 7 green, 2 blue, 2 red

    for line in f:
        game_draws = line.split(":")
        game_num = int(game_draws[0].split("Game ")[1])
        draws = game_draws[1].split(";")

        games[game_num] = {"red": 0, "green": 0, "blue": 0 }

        for draw in draws:
            # [' 3 green', ' 1 blue', ' 3 red']
            # [' 3 blue', ' 1 green', ' 3 red']
            # [' 2 red', ' 12 green', ' 7 blue']
            # [' 1 red', ' 4 blue', ' 5 green']
            # [' 7 green', ' 2 blue', ' 2 red']

            count = ""
            color = ""

            for elem in draw.split(","):
                # ['3', 'green']
                count = int(elem.split()[0])
                color = elem.split()[1]

                if games[game_num][color] < count:
                    games[game_num][color] = count

    return games


def part1():
    '''
    only 12 red cubes, 13 green cubes, and 14 blue cubes
    '''

    all_games = process_games()
    valid_games = []

    for game in all_games.items():
        colors = game[1]
        if colors["red"] <= 12 and colors["green"] <= 13 and colors["blue"] <= 14:
            valid_games.append(game[0])

    print(sum(valid_games))


def part2():

    all_games = process_games()
    powers = []

    for game in all_games.items():
        colors = game[1]
        powers.append(colors["red"] * colors["green"] * colors["blue"])

    print(sum(powers))

if __name__ == "__main__":
    part1()
    print("---")
    part2()