# Advent of Code 2021 Solution
# By: Bailey Carothers
# For: Day 3, Part 1
# Objective:
# Inputs are structured as binary numbers. ex "01011"
# See requirements.txt for full explanation


if __name__ == "__main__":
    # Declare variables as needed by requirements
    onesFound = []
    zerosFound = []
    gamma = ""
    epsilon = ""
    totalLines = 0

    with open("input.txt", "r") as infile:
        # Find the length of our first line to determine input length
        firstLine = infile.readline()
        listLength = len(firstLine) - 1
        binarySize = listLength
        # Add 0's to our lists for the appropriate length
        for x in range(0, listLength, 1):
            onesFound.append(0)
            zerosFound.append(0)

        # Reset our position to first line again
        infile.seek(0, 0)

        # Iterate through file line by line
        for line in infile:
            for x in range(0, binarySize, 1):
                if line[x] == "1":
                    onesFound[x] += 1
                else:
                    zerosFound[x] += 1
            totalLines += 1
    infile.close()

    for x in range(0, binarySize, 1):
        if zerosFound[x] > onesFound[x]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    finalAnswer = int(gamma, 2) * int(epsilon, 2)

    # Write answer to output.txt
    with open("output.txt", "w") as outfile:
        outfile.write(str(finalAnswer))
    outfile.close()
