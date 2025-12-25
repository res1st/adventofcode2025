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

sum = 0
for line in linesFile:
    line = line.strip()
    totalPower = 0
    length = len(line)
    print(f"line {line}")

    max = calulateMaxOfLine(line, 0, length-1)
    max2nd = calulateMaxOfLine(line, max["index"] + 1, length)

    intValue = int(max["max"] + max2nd["max"])
    print(f"Max value is {intValue}")
    sum += intValue
    
    
print(f"Total Power Consumption: {sum}")

