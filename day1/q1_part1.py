import re
import os 
value = 50


number_of_times_zero_happened = 0
with open("day1/q1_input", "r") as file:
    for line in file:
        instruction = re.match(r"([RL])(\d+)", line.strip()).groups()
        direction = instruction[0]
        steps = int(instruction[1])

        if direction == "R":
            value += steps
        elif direction == "L":
            value -= steps
        
        value = value % 100
        if value == 0:
            number_of_times_zero_happened += 1

print("Number of times value reached zero:", number_of_times_zero_happened)