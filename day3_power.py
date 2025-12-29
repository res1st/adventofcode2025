# Day 3: Power Consumption
# https://adventofcode.com/2025/day/3

input = """987654321111111
811111111111119
234234234234278
818181911112111
"""

lines = input.strip().split("\n")

with open("inputs/day3.txt","r") as file:
    linesFile = file.readlines()

def calulateMaxOfLine(line, startIndex, endIndex):
    maxValue = 0
    maxIndex = 0
    for i in range(startIndex, endIndex):
        currentValue = int(line[i])
        if currentValue > maxValue:
            maxValue = currentValue
            maxIndex = i
        # print(f"i={i}  currentValue={currentValue}  maxValue={maxValue}")
    return {"max": str(maxValue), "index": maxIndex}

def part1():
    sum = 0
    for line in linesFile:
        line = line.strip()
        length = len(line)
        print(f"line {line}")

        max = calulateMaxOfLine(line, 0, length-1)
        max2nd = calulateMaxOfLine(line, max["index"] + 1, length)

        intValue = int(max["max"] + max2nd["max"])
        print(f"Max value is {intValue}")
        sum += intValue
        
        
    print(f"Total Power Consumption: {sum}")

# doesn't produce the biggest possible number
# it removes the smallest digit regardless of position, which is wrong
def removeLowestUntil12Digits(line):
    while len(line) > 12:
        minValue = 10
        minIndex = -1
        for i in range(len(line)):
            currentValue = int(line[i])
            if currentValue < minValue:
                minValue = currentValue
                minIndex = i
        line = line[:minIndex] + line[minIndex+1:]
    return line

# monotonic stack
# removes the previous digit if the current digit is larger
def removeLowestUntil12DigitsWithStack(line):
    targetLength = 12
    numberOfDigitsToRemove = len(line) - targetLength
    stack = []

    for digit in line:
        # While we still have removals left AND the stack isn't empty 
        # AND the current digit is bigger than the last one added...
        while numberOfDigitsToRemove > 0 and stack and stack[-1] < digit:
            stack.pop()
            numberOfDigitsToRemove -= 1
        stack.append(digit)
    
    # If we still need to remove digits (e.g., input was "999999999999999"),
    # remove them from the end.
    result = "".join(stack[:targetLength])
    return result

def part2():
    sum = 0
    for line in linesFile:
        line = line.strip()
        length = len(line)
        print(f"line {line}")

        firstMax = calulateMaxOfLine(line, 0, length-11)
        print(f"First max value is {firstMax['max']} at index {firstMax['index']}")
        totalMaxValue = line[firstMax["index"]:]
        print(f"Total max value is {totalMaxValue}")
        max12DigitsValue = removeLowestUntil12DigitsWithStack(totalMaxValue)
        print(f"12 digits value is {max12DigitsValue}")
        
        print("----")
        sum += int(max12DigitsValue)
        
    print(f"Total Power Consumption (Part 2): {sum}")

part2()
