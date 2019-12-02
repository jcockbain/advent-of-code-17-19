from collections import defaultdict
import string
import re

input = open('input.txt').readlines()
input_list = []
for line in input:
    a, b = re.findall(r' ([A-Z]) ', line)
    input_list.append((a, b))


def part_1(rules):
    tasks = set()
    deps = defaultdict(set)
    for rule in rules:
        a, b = rule
        tasks |= {a, b}
        deps[b].add(a)
    done = []
    for _ in tasks:
        done.append(
            min(x for x in tasks if x not in done and deps[x] <= set(done)))
    return ''.join(done)


def part_2(points):
    pass


print(part_1(input_list))
