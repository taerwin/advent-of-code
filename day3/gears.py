import sys
import re
import numpy as np

sum = 0
mask = None


# Read file
with open(sys.argv[1]) as f:
    lines = f.readlines()

# Find all '*'
for i,line in enumerate(lines):
    symbols = [True if c in "*" else False for c in line.strip()]

    if i == 0:
        mask = np.array(symbols, dtype=bool)
    else:
        mask = np.vstack([mask, symbols])

ratios = np.zeros(mask.shape, dtype=int)
for i,line in enumerate(lines):
    for match in re.finditer(r'\d+', line):
        start,end = match.span()
        row_start = max(0,start-1)
        row_end = min(end+1, len(line))
        col_start = max(0,i-1)
        col_end = min(i+2, len(lines))

        # Number is next to '*'
        # Indexing is messy :(
        if np.any(mask[col_start:col_end,row_start:row_end]):
            j,k = np.where(mask[col_start:col_end,row_start:row_end])
            if i <= 1:
                j = j[0]
            else:
                j = j[0] + i - 1
            if row_start == 0:
                k = k[0]
            else:
                k = k[0] + start - 1
            if ratios[j,k] != 0:
                # multiply
                ratios[j,k] = ratios[j,k] * int(match.group())
                sum += ratios[j,k]
            else:
              ratios[j,k] = int(match.group())

print(sum)