import re

from dataclasses import dataclass

FILENAME = "input"

max_line = 139
max_position = 139

@dataclass
class Number():
    value: int
    line_id: int
    start_position: int
    end_position: int

    def symbols_coords(self):
        coords = []

        if self.line_id != 0:
            if self.start_position != 0:
                coords.append([self.line_id - 1, self.start_position - 1])
            for i in range(self.start_position, self.end_position):
                coords.append([self.line_id - 1, i])
            if self.end_position != max_position:
                coords.append([self.line_id - 1, self.end_position])

        if self.line_id != max_line:
            if self.start_position != 0:
                coords.append([self.line_id + 1, self.start_position - 1])
            for i in range(self.start_position, self.end_position):
                coords.append([self.line_id + 1, i])
            if self.end_position != max_position:
                coords.append([self.line_id + 1, self.end_position])

        if self.start_position != 0:
            coords.append([self.line_id, self.start_position - 1])
        
        if self.end_position != max_position:
            coords.append([self.line_id, self.end_position])

        return coords

def is_symbol_adjacent(number, symbols):
    for coord in number.symbols_coords():
        if coord in symbols:
            return True
    return False

# def does_string_starts_with_symbol(my_string):
#     pass

# def does_string_ends_with_symbol(my_string):
#     pass

with open(FILENAME, "r") as f:
    inputs = f.read().splitlines()

    numbers = [] # List of Number
    symbols = [] # List of symbols coordinates
    
    line_id = 0
    for input in inputs:
        position_number = 0
        position_symbol = 0
        # get_max_line_length

        elements = re.split(r'(\d+)', input)
        # re.split(r'(\d+)',"12..34..56..")
        # ['', '12', '..', '34', '..', '56', '..']
        # Using groups = numbers are also included in the list
        # Always a uneven number of elements (minimum 1):
        # Always (str, int, str, int, str .... str)

        # first_string = True
        try:
            while True:
                string_before_number = elements.pop(0)
                # if not first_string and does_string_starts_with_symbol(string_before_number):
                #     numbers.pop()
                # first_string = False

                number_value = elements.pop(0) # Can raise IndexError
                start_position = position_number + len(string_before_number)
                end_position = start_position + len(number_value)
                # if not does_string_ends_with_symbol(string_before_number):

                numbers.append(
                    Number(
                        value=int(number_value),
                        line_id=line_id,
                        start_position=start_position,
                        end_position=end_position,
                    )
                )

                position_number = end_position
        except IndexError: # raised by pop if end of list
            pass

        # re.split('([^a-zA-Z0-9.])+',"12...*...34#..56..$78~")
        # ['12...', '*', '...34', '#', '..56..', '$', '78', '~', '']

        elements = re.split('([^a-zA-Z0-9.])+',input)
        try:
            while True:
                string_before_symbol = elements.pop(0)
                _ = elements.pop(0) # Can raise IndexError
                start_position = position_symbol + len(string_before_symbol)
                symbols.append([line_id, start_position])

                position_symbol = start_position+1
        except IndexError: # raised by pop if end of list
            pass

        line_id += 1

total_sum = 0

for number in numbers:
    if is_symbol_adjacent(number, symbols):
        print(f"Adding {number.value} to {total_sum}")
        total_sum += number.value

print(f"Total sum: {total_sum}")

# import pprint
# pprint.pprint(numbers)
# pprint.pprint(symbols)



# import pdb; pdb.set_trace()