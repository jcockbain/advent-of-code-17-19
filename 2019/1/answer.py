input = open('input.txt').readlines()
int_list = [int(x) for x in input]


def part_1(input):
    total = 0
    for value in input:
        total += int(value / 3) - 2
    return total


def part_2(input):
    total = 0
    for value in input:
        while value > 0:
            value = int(value / 3) - 2
            if value > 0:
                total += value
    return total


print(part_2(int_list))
