FILENAME = "input"

def get_prev_elem(my_list):

    diff_list = []
    all_zeros = True
    i = 0
    while i < len(my_list)-1:
        diff = my_list[i+1] - my_list[i]
        diff_list.append(diff)
        if diff != 0:
            all_zeros = False
        i += 1

    if all_zeros:
        # break recursion
        return my_list[0]

    return my_list[0] - get_prev_elem(diff_list) 

sum = 0
with open(FILENAME, "r") as f:
    inputs = f.read().splitlines()
    
    for input in inputs:
        list_of_nums = []
        for elem in input.split():
            list_of_nums.append(int(elem))
        prev_elem = get_prev_elem(list_of_nums)
        sum += prev_elem

print(f"Sum: {sum}")