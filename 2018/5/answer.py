from collections import defaultdict
import string

input = open('input.txt').readlines()


def part_1(x):
    result = ['']
    for c in x:
        if c == result[-1].swapcase():
            result.pop()
        else:
            result.append(c)
    return len(''.join(result))


def part_2(x):
    letters = set(x.lower())
    return min(part_1(x.replace(c, '').replace(c.upper(), ''))
               for c in letters)


print(part_1(input[0]))
print(part_2(input[0]))
