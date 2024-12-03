from utils import *
from collections import Counter

DAY = 1
YEAR = 2024
data = get_input(write=True, day=DAY, year=YEAR)

# ------------------------------------------------------------------------------

data = [x for x in data.split('\n') if x]
list_1 = [int(x.split()[0]) for x in data]
list_2 = [int(x.split()[1]) for x in data]

ans_1 = 0
for a, b in zip(sorted(list_1), sorted(list_2)):
    ans_1 += abs(a - b)


list_2 = Counter(list_2)
ans_2 = 0
for x in list_1:
    ans_2 += x * list_2.get(x, 0)

# ------------------------------------------------------------------------------

submit(
    ans_1=ans_1,
    ans_2=ans_2,
    day=DAY,
    year=YEAR,
    show_rank=False
)
