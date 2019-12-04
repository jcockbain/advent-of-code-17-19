from collections import Counter


def is_password_1(num):
    num = str(num)
    return list(num) == sorted(num) and (Counter(num).most_common()[0][1]) >= 2


def is_password_2(num):
    num = str(num)
    return list(num) == sorted(num) and 2 in Counter(num).values()


if __name__ == '__main__':
    min = 136760
    max = 595730
    part1, part2 = 0, 0
    for i in range(min, max + 1):
        if is_password_1(i):
            part1 += 1
        if is_password_2(i):
            part2 += 1

    print('part 1: ', part1)
    print('part 2: ', part2)
