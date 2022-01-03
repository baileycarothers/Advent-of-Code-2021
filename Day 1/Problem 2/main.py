# Advent of Code 2021 Solution
# By: Bailey Carothers
# For: Day 1, Part 2
# Objective: Read numbers from a file, sliding window of 3 comparison
# See requirements.txt for full explanation

if __name__ == '__main__':
    increasesFound = 0
    # Read our input file line by line
    with open("input.txt", "r") as infile:
        numArray = []
        lineNum = 0
        for line in infile:
            numArray.append(int(line))

        a = 0
        b = 0
        c = 0
        numAdded = 0

        for x in range(0, len(numArray)):
            if numAdded == 0:
                a += numArray[x]
                numAdded += 1
            elif numAdded == 1:
                a += numArray[x]
                b += numArray[x]
                numAdded += 1
            elif numAdded == 2:
                a += numArray[x]
                b += numArray[x]
                c += numArray[x]
                numAdded += 1

        increasesFound = a

        # Write answer to output.txt
        with open("output.txt", "w") as outfile:
            outfile.write(str(increasesFound))
        outfile.close()
