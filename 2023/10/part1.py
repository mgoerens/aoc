FILENAME = "input"

from contextlib import suppress

def find_start(grid):
    grid_x_length = range(len(grid[0]))
    grid_y_length = range(len(grid))

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

with open(FILENAME, "r") as f:
    grid = f.read().splitlines()

    start_x, start_y = find_start(grid)          

    print(f"Start x={start_x}; y={start_y}")
    next_x_hop, next_y_hop, source = find_first_hop(grid, start_x, start_y)
    steps = 1
    
    while grid[next_x_hop][next_y_hop] != "S":
        print(f"next hop x={next_x_hop}; y={next_y_hop}; value={grid[next_x_hop][next_y_hop]}")
        next_x_hop, next_y_hop, source = find_next_hop(grid, next_x_hop, next_y_hop, source)
        steps += 1

    print(f"Total steps: {steps}")
    print(f"Most remote tile: {steps/2}")