FILENAME = "input"

def get_info(line):
    _, items = line.split(":")
    return int("".join(items.split()))

with open(FILENAME, "r") as f:
    inputs = f.read().splitlines()

    time = get_info(inputs[0])
    dist = get_info(inputs[1])

    possible_wins = 0

    for i in range(time):
        pushed_time = i
        speed = i
        movement_time = time - i

        distance = speed * movement_time

        if distance > dist:
            possible_wins += 1

print(f"Possible Wins: {possible_wins}")