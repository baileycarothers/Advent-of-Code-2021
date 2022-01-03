# Advent of Code 2021 Solution
# By: Bailey Carothers
# For: Day 2, Part 2
# Objective: Find displacement of a submarine based on given inputs
# Inputs are structured as "forward 7"
# See requirements.txt for full explanation


if __name__ == "__main__":
    # Declare variables as needed by requirements
    horizontal = 0
    depth = 0
    aim = 0

    # Open the file and go line by line
    with open("input.txt", "r") as infile:
        for line in infile:
            # Split divides strings at whitespace by default, result is a list
            input = line.split()
            # Horizontal is modified by forward
            # Depth is modified by our aim and our directional movement
            if input[0] == "forward":
                horizontal += int(input[1])
                depth += int(input[1]) * aim
            # Up and down modify our "aim" for the nose of the submarine
            elif input[0] == "up":
                aim -= int(input[1])
            elif input[0] == "down":
                aim += int(input[1])
            else:
                print("Input file formatted incorrectly")
    infile.close()

    # Do some math with our x and y
    finalDistance = horizontal * depth

    # Write answer to output.txt
    with open("output.txt", "w") as outfile:
        outfile.write(str(finalDistance))
    outfile.close()
