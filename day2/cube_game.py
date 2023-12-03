import regex
import sys

sum = 0
power = 0

red_cubes = 12
green_cubes = 13
blue_cubes = 14

# Read file
input = open(sys.argv[1], 'r')

for i,line in enumerate(input):
    red = regex.findall(r'(\d+) red', line)
    green = regex.findall(r'(\d+) green', line)
    blue = regex.findall(r'(\d+) blue', line)
    # max red cubes
    max_red = max([int(r) for r in red])
    max_blue = max([int(b) for b in blue])
    max_green = max([int(g) for g in green])

    if max_red <= red_cubes and \
       max_green <= green_cubes and \
       max_blue <= blue_cubes:
        sum += i+1

    power += max_red * max_blue * max_green

input.close()
print(sum)
print(power)
