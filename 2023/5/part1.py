FILENAME = "input"

class Seed():
    seed_value: int
    intermediate_value: int
    location_value: int
    is_translated: bool

    def __init__(self, value):
        self.seed_value = value
        self.intermediate_value = value
        self.is_translated = False

tm_list = []
with open(FILENAME, "r") as f:
    inputs = f.read().splitlines()

    seeds_line = True
    seeds = []

    for input in inputs:
        if seeds_line:
            # First line
            _, seeds_str = input.split(": ")
            seeds_list = seeds_str.split()
            seeds_line = False

            for seed in seeds_list:
                seeds.append(Seed(int(seed)))
            continue

        if input == "": # Ingore empty lines
            continue

        if not input[0].isdigit():
            for seed in seeds:
                seed.is_translated = False

        else:
            dest_start_range = int(input.split()[0])
            source_start_range =int(input.split()[1])
            length = int(input.split()[2])

            for seed in seeds:
                if source_start_range <= seed.intermediate_value & seed.intermediate_value < source_start_range + length:
                    if not seed.is_translated:
                        seed.intermediate_value = dest_start_range + (seed.intermediate_value - source_start_range)
                        seed.is_translated = True


    min_location = None
    first_seed = True
    for seed in seeds:
        seed_location = seed.intermediate_value
        if first_seed or seed_location < min_location:
            first_seed = False
            min_location = seed_location

    print(f"Min location: {min_location}")