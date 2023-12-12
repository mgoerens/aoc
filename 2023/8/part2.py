FILENAME = "input"

class ReachedZZZException(Exception):
    pass

with open(FILENAME, "r") as f:
    inputs = f.read().splitlines()

    LR_instructions = inputs[0]
    nodes = {}

    current_nodes = []

    for input in inputs[2:]:
        node_source, targets = input.split(" = ")
        targetL = targets[1:4]
        targetR = targets[6:9]

        nodes[node_source] = [targetL, targetR]
        if node_source[-1] == "A":
            current_nodes.append(node_source)

steps = 0
try:
    while True:
        # print(steps)
        # print(current_nodes)
        for instruct in LR_instructions:
            steps += 1

            ended = 0
            for i, cn in enumerate(current_nodes):
                if instruct == "L":
                    current_nodes[i] = nodes[cn][0]
                else:
                    current_nodes[i] = nodes[cn][1]
                
                if current_nodes[i][-1] == "Z":
                    print(f"node {i} has ended on step {steps}; reached {current_nodes[i]}")
                    ended += 1
            
            if ended == len(current_nodes):
                raise ReachedZZZException
except ReachedZZZException:
    pass

print(f"Steps: {steps}")
