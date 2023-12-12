FILENAME = "input"

def print_map(map):
    for row in map:
        for elem in row:
            print(f"{elem}", end='')
        print("")


def expand_lines(map):
    map_with_lines_expanded = []
    for i in range(len(map)):
        map_with_lines_expanded.append(map[i])
        for j in range(len(map[0])):
            if map[i][j] == "#":
                break
        else: #didn't break = no galaxy = expanding
            map_with_lines_expanded.append(map[i])
    return map_with_lines_expanded

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

def expand_map(map):
    y_expanded_map = expand_lines(map)
    # print("y_expanded_map")
    # print_map(y_expanded_map)

    rotated_y_expanded_map = rotate_left(y_expanded_map)
    # print("rotated_y_expanded_map")
    # print_map(rotated_y_expanded_map)

    rotated_xy_expanded_map = expand_lines(rotated_y_expanded_map)
    # print("rotated_xy_expanded_map")
    # print_map(rotated_xy_expanded_map)

    return rotated_xy_expanded_map

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

    expanded_map = expand_map(map)

    coords = get_galax_coords(expanded_map)

    dist = 0

    try:
        while True:
            source = coords.pop() # get a galaxy
            for galaxy in coords:
                dist += abs(source[0] - galaxy[0]) + abs(source[1] - galaxy[1])
    except IndexError:
        # no more galaxy to pop
        pass


    print(f"Total distance: {dist}")