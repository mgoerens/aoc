FILENAME = "input"

class ReachedZZZException(Exception):
    pass

with open(FILENAME, "r") as f:
    inputs = f.read().splitlines()

    LR_instructions = inputs[0]
    nodes = {}

    for input in inputs[2:]:
        node_source, targets = input.split(" = ")
        targetL = targets[1:4]
        targetR = targets[6:9]

        nodes[node_source] = [targetL, targetR]

current_node = "AAA"
steps = 0
try:
    while True:
        for instruct in LR_instructions:
            steps += 1
            if instruct == "L":
                current_node = nodes[current_node][0]
            else:
                current_node = nodes[current_node][1]

            if current_node == "ZZZ":
                raise ReachedZZZException
except ReachedZZZException:
    pass

print(f"Steps: {steps}")
