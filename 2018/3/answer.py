import collections
import re

input = open('input.txt').readlines()
input_list = [x.rstrip('\n') for x in input]


def part_1(input):
    ids = get_ids(input)
    return sum(len(x) > 1 for x in ids.values())


def part_2(input):
    ids = get_ids(input)
    all_ids = set()
    invalid_ids = set()
    for x in ids.values():
        all_ids |= x
        if len(x) > 1:
            invalid_ids |= x
    return all_ids - invalid_ids


def get_ids(input):
    ids = collections.defaultdict(set)
    for line in input:
        id, x, y, w, h = map(int, re.findall(r'\d+', line))
        for j in range(y, y + h):
            for i in range(x, x + w):
                ids[(i, j)].add(id)
    return ids


print(part_1(input_list))
print(part_2(input_list))
