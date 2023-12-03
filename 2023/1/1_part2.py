
def replace_str_to_int(input):
    print(f"Replacing str to int for {input}")

    # # corner cases:
    # input = input.replace("oneight", "18")
    # input = input.replace("twone", "21")
    # input = input.replace("threeight", "38")
    # input = input.replace("fiveeight", "58")
    # input = input.replace("sevenine", "79")
    # input = input.replace("eightwo", "82")
    # input = input.replace("eighthree", "83")
    # input = input.replace("nineight", "98")
    # # input = input.replace("zerone", "01")

    input = input.replace("one", "one1one")
    input = input.replace("two", "two2two")
    input = input.replace("three", "three3three")
    input = input.replace("four", "four4four")
    input = input.replace("five", "five5five")
    input = input.replace("six", "six6six")
    input = input.replace("seven", "seven7seven")
    input = input.replace("eight", "eight8eight")
    input = input.replace("nine", "nine9nine")
    # input = input.replace("zero", "0")

    print(f"Result replacing: {input}")
    
    return input


total_sum = 0

with open("1.input", "r") as f:
    inputs = f.readlines()
    for input in inputs:
        input = replace_str_to_int(input)

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