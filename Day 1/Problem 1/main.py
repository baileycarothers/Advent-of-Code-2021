# Advent of Code 2021 Solution
# By: Bailey Carothers
# For: Day 1, Part 1
# Objective: Read numbers from a file, count how many are higher than the previous
# See requirements.txt for full explanation

if __name__ == '__main__':
    increasesFound = 0
    # Read our input file line by line
    with open("input.txt", "r") as infile:
        # Read first line only into prevNum
        prevNum = int(infile.readline())
        newNum = 0
        # Rereading the first line is minuscule enough to leave
        for line in infile:
            # Read next number into newNum
            newNum = int(line)
            # Check for increase in depth (number)
            if newNum > prevNum:
                increasesFound += 1
            # Make prevNum our current num for next iteration
            prevNum = newNum
    infile.close()

    # Write answer to output.txt
    with open("output.txt", "w") as outfile:
        outfile.write(str(increasesFound))
    outfile.close()
