FILENAME = "input"

def get_info(line):
    _, items = line.split(":")
    return items.split()

with open(FILENAME, "r") as f:
    inputs = f.read().splitlines()

    time_table = get_info(inputs[0])
    dist_table = get_info(inputs[1])

    product = 1
    for index, time in enumerate(time_table):
        possible_wins = 0

        for i in range(int(time)):
            pushed_time = i
            speed = i
            movement_time = int(time) - i

            distance = speed * movement_time

            if distance > int(dist_table[index]):
                possible_wins += 1

        product *= possible_wins

print(f"Product: {product}")