FILENAME = "input"

from contextlib import suppress

def find_start(grid):
    grid_x_length = range(len(grid))
    grid_y_length = range(len(grid[0]))

    for i in grid_x_length:
        for j in grid_y_length:
            if grid[i][j] == "S":
                return i, j

def find_first_hop(grid, start_x, start_y):
    # search north
    with suppress(IndexError): # corner case: Start on the border of grid
        if grid[start_x-1][start_y] in ["7", "|", "F"]:
            # found match
            return start_x-1, start_y, "S"
    
    # search south
    with suppress(IndexError): # corner case: Start on the border of grid
        if grid[start_x+1][start_y] in ["J", "|", "L"]:
            # found match
            return start_x+1, start_y, "N"

    # search east = right
    with suppress(IndexError): # corner case: Start on the border of grid
        if grid[start_x][start_y+1] in ["J", "-", "7"]:
            # found match
            return start_x, start_y+1, "W"

    # search west = left
    with suppress(IndexError): # corner case: Start on the border of grid
        if grid[start_x][start_y-1] in ["L", "-", "F"]:
            # found match
            return start_x, start_y+1, "E"

def find_next_hop(grid, next_x_hop, next_y_hop, source):
    if source == "N":
        if grid[next_x_hop][next_y_hop] == "J":
            return next_x_hop, next_y_hop-1, "E"
        if grid[next_x_hop][next_y_hop] == "|":
            return next_x_hop+1, next_y_hop, "N"
        if grid[next_x_hop][next_y_hop] == "L":
            return next_x_hop, next_y_hop+1, "W"

    if source == "S":
        if grid[next_x_hop][next_y_hop] == "7":
            return next_x_hop, next_y_hop-1, "E"
        if grid[next_x_hop][next_y_hop] == "|":
            return next_x_hop-1, next_y_hop, "S"
        if grid[next_x_hop][next_y_hop] == "F":
            return next_x_hop, next_y_hop+1, "W"

    if source == "W":
        if grid[next_x_hop][next_y_hop] == "J":
            return next_x_hop-1, next_y_hop, "S"
        if grid[next_x_hop][next_y_hop] == "-":
            return next_x_hop, next_y_hop+1, "W"
        if grid[next_x_hop][next_y_hop] == "7":
            return next_x_hop+1, next_y_hop, "N"

    if source == "E":
        if grid[next_x_hop][next_y_hop] == "L":
            return next_x_hop-1, next_y_hop, "S"
        if grid[next_x_hop][next_y_hop] == "-":
            return next_x_hop, next_y_hop-1, "E"
        if grid[next_x_hop][next_y_hop] == "F":
            return next_x_hop+1, next_y_hop, "N"

def replace_source_tile(source_goes_to, source_comes_from):
    if (source_comes_from == "S") & (source_goes_to == "S"):
        return "|"
    if (source_comes_from == "N") & (source_goes_to == "N"):
        return "|"
    if (source_comes_from == "W") & (source_goes_to == "W"):
        return "-"
    if (source_comes_from == "E") & (source_goes_to == "E"):
        return "-"
    if (source_comes_from == "W") & (source_goes_to == "N"):
        return "L"
    if (source_comes_from == "S") & (source_goes_to == "E"):
        return "L"
    if (source_comes_from == "W") & (source_goes_to == "S"):
        return "F"
    if (source_comes_from == "N") & (source_goes_to == "E"):
        return "F"
    if (source_comes_from == "E") & (source_goes_to == "N"):
        return "J"
    if (source_comes_from == "S") & (source_goes_to == "W"):
        return "J"
    if (source_comes_from == "E") & (source_goes_to == "S"):
        return "7"
    if (source_comes_from == "N") & (source_goes_to == "W"):
        return "7"

def toggle_bool(my_bool):
    return not my_bool

with open(FILENAME, "r") as f:
    grid = f.read().splitlines()

    start_x, start_y = find_start(grid)
    pipe = [[start_x, start_y]]
    min_x = start_x
    max_x = start_x
    min_y = start_y
    max_y = start_y

    # print(f"Start x={start_x}; y={start_y}")
    next_x_hop, next_y_hop, source = find_first_hop(grid, start_x, start_y)
    source_comes_from = source

    steps = 1
    while grid[next_x_hop][next_y_hop] != "S":
        # print(f"next hop x={next_x_hop}; y={next_y_hop}; value={grid[next_x_hop][next_y_hop]}")
        pipe.append([next_x_hop, next_y_hop])
        next_x_hop, next_y_hop, source = find_next_hop(grid, next_x_hop, next_y_hop, source)
        steps += 1

        if next_x_hop < min_x:
            min_x = next_x_hop
        if next_x_hop > max_x:
            max_x = next_x_hop
        if next_y_hop < min_y:
            min_y = next_y_hop
        if next_y_hop > max_y:
            max_y = next_y_hop
            

    grid[start_x] = grid[start_x][0:start_y] + replace_source_tile(source, source_comes_from) + grid[start_x][start_y+1:]

    enclosed = 0
    i = min_x
    while i <= max_x:
        j = min_y
        is_inside = False
        source = None
        while j <= max_y:
            # print(f"Checking tile {i}, {j}. is_inside={is_inside}; source={source}; value={grid[i][j]}")

            if not [i, j] in pipe:
                if is_inside:
                    enclosed += 1
                    # print(f"Tile {i}, {j} is enclosed")
            else:
                # Left start
                if grid[i][j] == "|":
                    is_inside = toggle_bool(is_inside)
                elif grid[i][j] == "F":
                    source = "S"
                elif grid[i][j] == "L":
                    source = "N"
                
                # ignore "-"
                elif (grid[i][j] == "J") & (source == "S"):
                    is_inside = toggle_bool(is_inside)
                elif (grid[i][j] == "7") & (source == "N"):
                    is_inside = toggle_bool(is_inside)
            j+=1
        i+=1
    
    print(f"Enclosed: {enclosed}")