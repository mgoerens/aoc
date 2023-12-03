total_sum = 0

AMOUNT_RED = 12
AMOUNT_GREEN = 13
AMOUNT_BLUE = 14

def get_game_id(game_info):
    _, id = game_info.split(" ")
    print(f"Found game ID: {id}")
    return int(id)

def check_results(results):
    for result in results:
        cubes_info = result.split(", ")
        # ['1 red', '2 green', '6 blue']

        for cubes in cubes_info:
            amount, color = cubes.split(" ")
            print(amount, color)

            if color == "red":
                if int(amount) > AMOUNT_RED:
                    return False

            if color == "blue":
                if int(amount) > AMOUNT_BLUE:
                    return False

            if color == "green":
                if int(amount) > AMOUNT_GREEN:
                    return False

    return True


with open("input", "r") as f:
    inputs = f.read().splitlines()
    for input in inputs:
        print(f"Processing game input: {input}")

        game_info, results_info = input.split(": ")
        # ['Game 1', ' 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green']
        game_id = get_game_id(game_info)

        results = results_info.split("; ")
        # [' 3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']

        is_game_possible = check_results(results)
        
        if is_game_possible:
            print("Game is possible, adding up")
            total_sum += game_id
        
        print(f"current sum is {total_sum}")

print(f"Total sum: {total_sum}")
