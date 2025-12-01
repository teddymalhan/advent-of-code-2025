import re
import os 
value = 50


number_of_times_zero_happened = 0
with open("q1_input", "r") as file:
    for line in file:
        instruction = re.match(r"([RL])(\d+)", line.strip()).groups()
        direction = instruction[0]
        steps = int(instruction[1])

        if direction == "R":
            value += steps
        elif direction == "L":
            value -= steps
        
        oldvalue = value
        value = ((value % 100) + 100) % 100  # Keep value within 0-99 range

        # Check if value reached zero
        if oldvalue != value or value == 0:
            number_of_times_zero_happened += 1

print("Number of times value reached zero:", number_of_times_zero_happened)
