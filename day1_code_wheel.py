print("Day 1")

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

dialer = 50
zeros = 0

for line in inputSplitted:
    direction = line[0]
    clicks = int(line[1:])
    print(f"{direction} -> {clicks}")

    # didn't work because there are dials > 100 like 150    
    # if direction == 'R':
    #     dialer += clicks
    #     if (dialer > 99):
    #         dialer -= 100
    # else:
    #     dialer -= clicks
    #     if (dialer < 0):
    #         dialer +=100

    if direction == 'R':
        dialer = (dialer + clicks) % 100
    else:
        dialer = (dialer - clicks) % 100
                
    print(dialer)    
    if (dialer == 0):
        zeros +=1

print(f"Number of zero results is {zeros}")
