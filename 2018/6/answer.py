from collections import defaultdict
import string
import re

input = open('input.txt').readlines()
input_list = [x.rstrip('\n') for x in input]
input_tuples = [tuple(map(int, re.findall(r'\d+', x))) for x in input_list]


def part_1(points):
    counts = defaultdict(int)
    infinite = set()
    min_x, max_x = find_min_and_max_x(points)
    min_y, max_y = find_min_and_max_y(points)
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            ds = sorted((dist(x, y, px, py), i)
                        for i, (px, py) in enumerate(points))
            if ds[0][0] != ds[1][0]:
                counts[ds[0][1]] += 1
                if x == min_x or y == min_y or x == max_x or y == max_y:
                    infinite.add(ds[0][1])
    for k in infinite:
        counts.pop(k)
    return max(counts.values())


def part_2(x):
    pass


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def find_min_and_max_x(points):
    return min(x for x, y in points), max(x for x, y in points)


def find_min_and_max_y(points):
    return min(y for x, y in points), max(y for x, y in points)


data = [(1, 2), (3, 2), (3, 3), (2, 2)]
print(part_1(input_tuples))
