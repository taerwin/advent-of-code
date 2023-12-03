import sys
import re
import numpy as np

sum = 0
mask = None


# Read file
with open(sys.argv[1]) as f:
    lines = f.readlines()

for i,line in enumerate(lines):
    symbols = [True if c in "~!@#$%^&*()-+=/\\" else False for c in line.strip()]

    if i == 0:
        mask = np.array(symbols, dtype=bool)
    else:
        mask = np.vstack([mask, symbols])

for i,line in enumerate(lines):
    for match in re.finditer(r'\d+', line):
        print(match.group(), match.span())
        start,end = match.span()
        row_start = max(0,start-1)
        row_end = min(end+1, len(line))
        col_start = max(0,i-1)
        col_end = min(i+2, len(lines))
        if np.any(mask[col_start:col_end,row_start:row_end]):
            sum += int(match.group())

print(sum)