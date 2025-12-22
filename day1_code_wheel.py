inputTest = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

with open("inputs/day1.txt","r") as f:
    input = f.read()

inputSplitted = input.splitlines()

def part1():
    dialer = 50
    zeros = 0
    
    for line in inputSplitted:
        direction = line[0]
        clicks = int(line[1:])
        print(f"{direction} -> {clicks}")

        if direction == 'R':
            dialer = (dialer + clicks) % 100
        else:
            dialer = (dialer - clicks) % 100
                    
        print(dialer)    
        if (dialer == 0):
            zeros +=1
    return zeros

def part2():
    dialer = 50
    zeros = 0
    
    for line in inputSplitted:
        direction = line[0]
        clicks = int(line[1:])
        print(f"{direction} -> {clicks}")

        for _ in range(clicks):
            if direction == 'R':
                dialer = (dialer + 1) % 100
            else:
                dialer = (dialer - 1) % 100
            
            if dialer == 0:
                zeros += 1

    return zeros

# zeros = part1()
zeros = part2()

print(f"Number of zero results is {zeros}")

