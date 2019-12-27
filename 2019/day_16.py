def multiplier(n, m):
    m += 1
    m %= 4 * n
    if m < n:
        return 0
    elif m < 2 * n:
        return 1
    elif m < 3 * n:
        return 0
    elif m < 4 * n:
        return -1


def multiply(values, idx):
    idx += 1
    res = 0
    for i in range(len(values)):
        res += values[i] * multiplier(idx, i)
    return int(str(res)[-1:])


def add_phase(values):
    return [multiply(values, i) for i in range(len(values))]


def p1(values):
    data = [int(x) for x in values]
    for _ in range(100):
        data = add_phase(data)
    return int("".join(map(str, data[:8])))


def p2(values):
    data = [int(x) for x in values]
    return int("".join(map(str, data[:8])))


if __name__ == '__main__':
    file = open('inputs/16.in', 'r')
    data = file.read().strip()
    part1 = data[:]
    p_1 = p1(part1)
    print("part 1: ", p_1)
    part2 = data[:]
    p_2 = p2(part2)
    print("part 2:", p_2)
