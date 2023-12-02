import regex
import sys

#Calibration total
sum = 0

# Read file
filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    f.close()

for line in lines:
    two_digit = regex.search(r"^\D*(?P<first>\d).*(?P<last>\d)\D*$", line)
    single_digit = regex.search(r"^\D*(?P<first>\d)\D*$", line)
    if two_digit:
        sum += int(str(two_digit.group("first")) + str(two_digit.group("last")))
    if single_digit:
        sum += int(str(single_digit.group("first")) + str(single_digit.group("first")))

print(sum)

