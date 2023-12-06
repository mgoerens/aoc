FILENAME = "input"

total_sum = 0

with open(FILENAME, "r") as f:
    inputs = f.read().splitlines()

    for input in inputs:
        input_score = 0

        _, data = input.split(": ")
        data = " ".join(data.split()) # Remove double spaces

        winnings_data, results_data = data.split(" | ")

        winnings = winnings_data.split(" ")
        results = results_data.split(" ")

        for result in results:
            if result in winnings:
                if input_score == 0:
                    input_score = 1
                else:
                    input_score = input_score*2

        total_sum = total_sum + input_score

print(f"Total Sum: {total_sum}")