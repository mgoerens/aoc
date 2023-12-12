FILENAME = "input"
EXPANSION = 1000000

def print_map(map):
    for row in map:
        for elem in row:
            print(f"{elem}", end='')
        print("")


def get_empty_lines_index(map):
    empty_lines_index = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "#":
                break
        else: #didn't break = no galaxy = expanding
            empty_lines_index.append(i)
    return empty_lines_index

def rotate_left(map):
    rotated = []
    for i in range(len(map)): # y
        for j in range(len(map[0])): # x
            if i == 0:
                rotated.append([map[i][j]])
            else:
                rotated[j].append(map[i][j])
    return rotated

def rotate_right(map):
    rotated = []
    for j in range(len(map[0])):
        for i in range(len(map)):
            if i == 0:
                rotated.append([map[i][j]])
            else:
                rotated[j].append(map[i][j])
    return rotated

def get_empty_lines(map):
    y_empty_lines = get_empty_lines_index(map)
    # print("y_expanded_map")
    # print_map(y_expanded_map)

    rotated_map = rotate_left(map)
    # print("rotated_map")
    # print_map(rotated_map)

    x_empty_lines = get_empty_lines_index(rotated_map)
    # print("rotated_xy_expanded_map")
    # print_map(rotated_xy_expanded_map)

    return y_empty_lines, x_empty_lines

    # xy_rotated_map = rotate_right(rotated_xy_expanded_map)
    # print("xy_rotated_map")
    # print_map(xy_rotated_map)

    # return xy_rotated_map    

def get_galax_coords(map):
    coords = []
    for i, row in enumerate(map):
        for j, elem in enumerate(row):
            if elem == "#":
                coords.append([i, j])
    return coords

with open(FILENAME, "r") as f:
    map = f.read().splitlines()

    y_empty_lines, x_empty_lines = get_empty_lines(map)

    coords = get_galax_coords(map)

    dist = 0
    try:
        while True:
            source = coords.pop() # get a galaxy
            for galaxy in coords:
                dist += abs(source[0] - galaxy[0]) + abs(source[1] - galaxy[1])

                for y in y_empty_lines:
                    if y in range(min(source[0], galaxy[0]), max(source[0], galaxy[0])):
                        dist += EXPANSION - 1
                for x in x_empty_lines:
                    if x in range(min(source[1], galaxy[1]), max(source[1], galaxy[1])):
                        dist += EXPANSION - 1

    except IndexError:
        # no more galaxy to pop
        pass


    print(f"Total distance: {dist}")