# Advent of Code 2021 Solution
# By: Bailey Carothers
# For: Day 3, Part 1
# Objective:
# Inputs are structured as binary numbers. ex "01011"
# See requirements.txt for full explanation


if __name__ == "__main__":
    # Declare variables as needed by requirements
    inputList = []
    oxygen = []
    co2 = []

    with open("input.txt", "r") as infile:
        # Find the length of our first line to determine input length
        firstLine = infile.readline()
        binarySize = len(firstLine.strip())
        print(firstLine)
        print(binarySize)

        # Reset our position to first line again
        infile.seek(0, 0)

        # Iterate through line by line
        for line in infile:
            inputList.append(line.strip())
    infile.close()

    # Initialize to false so that we can fill our oxygen list from our input list once
    populated = False
    for y in range(0, binarySize, 1):
        oneFound = 0
        zeroFound = 0
        if len(oxygen) != 1:
            for x in range(0, len(oxygen), 1):
                if oxygen[x][y] == "1":
                    oneFound += 1
                else:
                    zeroFound += 1
            if oneFound >= zeroFound:
                careAbout = '1'
            else:
                careAbout = '0'
            # Our list only gets populated once based on first slot
            if not populated:
                for elem in list(inputList):
                    if elem[y] == careAbout:
                        oxygen.append(elem)
                populated = True
            # After population, every iteration removes irrelevant entries
            else:
                for elem in list(oxygen):
                    if elem[y] != careAbout:
                        oxygen.remove(elem)
        else:
            break

    populated2 = False
    for y in range(0, binarySize, 1):
        oneFound = 0
        zeroFound = 0
        if len(co2) != 1:
            for x in range(0, len(co2), 1):
                if co2[x][y] == "1":
                    oneFound += 1
                else:
                    zeroFound += 1
            if zeroFound <= oneFound:
                careAbout = '0'
            else:
                careAbout = '1'
            # Our list only gets populated once based on first slot
            if not populated2:
                for elem in list(inputList):
                    if elem[y] == careAbout:
                        co2.append(elem)
                populated2 = True
            # After population, every iteration removes irrelevant entries
            else:
                for elem in list(co2):
                    if elem[y] != careAbout:
                        co2.remove(elem)
        else:
            break

    # Iterate through and delete odd ones out
    finalAnswer = int(co2[0], 2) * int(oxygen[0], 2)
    print(oxygen)
    print(co2)
    print(finalAnswer)
    # Write answer to output.txt
    with open("output.txt", "w") as outfile:
        outfile.write(str(finalAnswer))
    outfile.close()
