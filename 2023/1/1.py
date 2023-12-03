

total_sum = 0
with open("1.input", "r") as f:
    inputs = f.readlines()
    for input in inputs:
        first_int = -1
        last_int = -1

        print(input)
        for i, c in enumerate(input):
            if c.isdigit():
                if first_int == -1:
                    first_int = c
                last_int = c
        print(f"Found first int = {first_int}")
        print(f"Found last int = {last_int}")

        comb = first_int + last_int
        print(f"Combination: {comb}")
        
        total_sum += int(comb)


print(f"Total Sum: {total_sum}")