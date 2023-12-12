FILENAME = "input"

# class Seed():
#     seed_value: int
#     intermediate_value: int
#     location_value: int
#     is_translated: bool

#     def __init__(self, value):
#         self.seed_value = value
#         self.intermediate_value = value
#         self.is_translated = False

# tm_list = []
with open(FILENAME, "r") as f:
    inputs = f.read().splitlines()


    # Parse first line
    # seeds = []
    _, seeds_str = inputs[0].split(": ")
    seeds_list = seeds_str.split()
    inputs.pop(0)
    min_location = 99999999999999999999999999999999999999999999999999999999999
    # first_seed = True
    maps = []
    mapss = []

    # Parse translation maps
    for input in inputs:
        if input == "": # Ingore empty lines
            continue

        if input[0].isdigit():
            dest_start_range = int(input.split()[0])
            source_start_range =int(input.split()[1])
            length = int(input.split()[2])

            maps.append([dest_start_range, source_start_range, length])

        else:
            mapss.append(maps)
            maps = []


    while True:
        try:
            seed_start = int(seeds_list.pop(0))
            seed_range = int(seeds_list.pop(0))

        except IndexError:
            break
        else:
            for i in range(seed_range):
                # seed = Seed(seed_start + i)
                seed_current_value = seed_start + i
                print(f"Processing seed {seed_current_value}")
            
                for maps in mapss:
                    seed_is_translated = False
                    for map in maps:
                        dest_start_range = map[0]
                        source_start_range = map[1]
                        length = map[2]

                        # print(f"Processing range: source_start {source_start_range}; dest_start {dest_start_range}; length {length}")
                        if (not seed_is_translated) & (source_start_range <= seed_current_value) & (seed_current_value < source_start_range + length):
                            # print(f"Found match for seed {seed_current_value}")
                            seed_current_value = dest_start_range + (seed_current_value - source_start_range)
                            seed_is_translated = True
                            # print(f"Seed translated to {seed_current_value}")

                        # for seed in seeds:
                        #     if not seed_is_translated:
                        #         print(f"Still no match for seed {seed_current_value}")

                seed_location = seed_current_value
                if seed_location < min_location:
                    # first_seed = False
                    min_location = seed_location

    print(f"Min location: {min_location}")