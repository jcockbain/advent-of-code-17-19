from collections import defaultdict
from operator import itemgetter
import re

input = open('input.txt').readlines()
input_list = [x.rstrip('\n') for x in input]


def part_1(input):
    totals, minutes = gen_structure(input)
    key = itemgetter(1)
    guard = max(totals.items(), key=key)[0]
    minute = max(minutes[guard].items(), key=key)[0]
    return guard * minute


def part_2(input):
    pass


def gen_structure(input):
    totals = defaultdict(int)
    minutes = defaultdict(lambda: defaultdict(int))
    for line in sorted(input):
        minute = int(re.search(r':(\d+)', line).group(1))
        if '#' in line:
            guard = int(re.search(r'#(\d+)', line).group(1))
        elif 'asleep' in line:
            m0 = minute
        elif 'wakes' in line:
            m1 = minute
            for m in range(m0, m1):
                totals[guard] += 1
                minutes[guard][m] += 1

    return totals, minutes


print(part_1(input_list))
