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
    # example eightwo shares the t so replace 
    # with text before and after number 
    line = str.replace(line, "one","one1one")
    line = str.replace(line, "two","two2two")
    line = str.replace(line, "three","three3three")
    line = str.replace(line, "four","four4four")
    line = str.replace(line, "five","five5five")
    line = str.replace(line, "six","six6six")
    line = str.replace(line, "seven","seven7seven")
    line = str.replace(line, "eight","eight8eight")
    line = str.replace(line, "nine","nine9nine")

    two_digit = regex.search(r"^\D*(?P<first>\d).*(?P<last>\d)\D*$", line)
    single_digit = regex.search(r"^\D*(?P<first>\d)\D*$", line)
    if two_digit:
        sum += int(str(two_digit.group("first")) + str(two_digit.group("last")))
    if single_digit:
        sum += int(str(single_digit.group("first")) + str(single_digit.group("first")))

print(sum)

