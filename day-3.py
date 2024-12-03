from utils import *

DAY = 3
YEAR = 2024
data = get_input(write=True, day=DAY, year=YEAR)

# ------------------------------------------------------------------------------

import re
mul_re = re.compile(r'mul\((\d+),(\d+)\)')

muls = re.findall(mul_re, data)
muls = [int(a) * int(b) for a, b in muls]
ans_1 = sum(muls)

mul_re = re.compile(r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)')
muls = re.findall(mul_re, data)

kept = []
keep = True
for entry in muls:
    if entry == 'do()':
        keep = True
    elif entry == "don't()":
        keep = False
    elif entry.startswith("mul("):
        if keep:
            kept.append(entry)
    else:
        raise ValueError(f"Unexpected entry: {entry}")

kept = [x.strip('mul()') for x in kept]
kept = [x.split(',') for x in kept]
kept = [int(x[0]) * int(x[1]) for x in kept]

ans_2 = sum(kept)

# ------------------------------------------------------------------------------

submit(
    ans_1=ans_1,
    ans_2=ans_2,
    day=DAY,
    year=YEAR,
    show_rank=False
)
