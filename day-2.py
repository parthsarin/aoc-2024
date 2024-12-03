from utils import *

DAY = 2
YEAR = 2024
data = get_input(write=True, day=DAY, year=YEAR)

# ------------------------------------------------------------------------------

data = [x for x in data.split('\n') if x]
data = [[int(x) for x in line.split()] for line in data]

def is_safe(row):
    dec = all(
        (a - b) in (1, 2, 3)
        for a, b in zip(row, row[1:])
    )
    inc = all(
        (a - b) in (-1, -2, -3)
        for a, b in zip(row, row[1:])
    )
    return dec or inc

ans_1 = 0
for row in data:
    ans_1 += is_safe(row)

ans_2 = 0
for row in data:
    ans_2 += any(
        is_safe(row[:i] + row[i + 1:])
        for i in range(len(row))
    )

# ------------------------------------------------------------------------------

submit(
    ans_1=ans_1,
    ans_2=ans_2,
    day=DAY,
    year=YEAR,
    show_rank=False
)
