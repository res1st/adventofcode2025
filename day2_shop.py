# riddle https://adventofcode.com/2025/day/2

input2 = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

with open("inputs/day2.txt","r") as file:
    input = file.read().strip()

inputSplitted = input.split(",")

part1sum = 0
for value in inputSplitted:
    bounds = value.split("-")
    lower = int(bounds[0])
    upper = int(bounds[1])

    for i in range(lower, upper + 1):
        # something like 1010
        valueAsString = str(i)
        length = len(valueAsString)
        isValid = True

        if length % 2 != 0:
            # only even numbers
            continue

        mid = length // 2
        if valueAsString[:mid] == valueAsString[mid:]:
            # first half must be the same as second half
            part1sum += i
print(f"Part 1 result is {part1sum}")

# part 2
part2Sum = 0
def findPattern(valueAsString):
    n = len(valueAsString)
    if not valueAsString:
        return None

    # (s + s)[1:-1] sucht nach dem String innerhalb seiner Verdopplung ohne die erste und letzte Nummer 
    index = (valueAsString + valueAsString).find(valueAsString, 1)

    if index != -1 and index < n:
        pattern = valueAsString[:index]
        # len is 12 and found index is 4 -> 3 times
        repeats = n // index
        return {
            "pattern": pattern,
            "count": repeats,
        }

for value in inputSplitted:

    bounds = value.split("-")
    lower = int(bounds[0])
    upper = int(bounds[1])

    for i in range(lower, upper + 1):
        foundPattern = findPattern(str(i))
        if foundPattern is not None:
            print(f"Value: {i} -> Pattern: {foundPattern}")
            part2Sum += i
print(f"Part 2 result is {part2Sum}")
