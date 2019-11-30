import collections

input = open('2.txt').readlines()
int_list = [x.rstrip('\n') for x in input]


def part_1(input):
    count_doubles = 0
    count_triples = 0
    for i in input:
        c = collections.Counter(i)
        values = c.values()
        if 2 in values:
            count_doubles += 1
        if 3 in values:
            count_triples += 1
    return count_doubles * count_triples


def part_2(input):
    pass


print(part_1(int_list))
