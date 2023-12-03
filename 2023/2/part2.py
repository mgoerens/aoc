total_sum = 0

def check_results(results):
    min_red = 0
    min_blue = 0
    min_green = 0

    for result in results:
        cubes_info = result.split(", ")
        # ['1 red', '2 green', '6 blue']

        for cubes in cubes_info:
            amount, color = cubes.split(" ")
            print(amount, color)

            if color == "red":
                if int(amount) > min_red:
                    min_red = int(amount)

            if color == "blue":
                if int(amount) > min_blue:
                    min_blue = int(amount)

            if color == "green":
                if int(amount) > min_green:
                    min_green = int(amount)

    return min_red * min_blue * min_green


with open("input", "r") as f:
    inputs = f.read().splitlines()
    for input in inputs:
        print(f"Processing game input: {input}")

        _, results_info = input.split(": ")
        # ['Game 1', ' 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green']

        results = results_info.split("; ")
        # [' 3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']

        power = check_results(results)

        total_sum += power
        
        print(f"current sum is {total_sum}")

print(f"Total sum: {total_sum}")
