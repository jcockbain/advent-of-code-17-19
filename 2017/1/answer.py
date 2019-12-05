def part_1(a):
    count = 0
    for i in range(0, len(a) - 1):
        if a[i] == a[i+1]:
            count += a[i]
        if a[0] == a[-1]:
            count += a[0]
    return count


def part_2(a):
    count = 0
    for i in range(0, len(a) - 1):
        next_index = int((i + (len(a) / 2)) % len(a))
        if a[i] == a[next_index]:
            count += a[i]
    return count


if __name__ == '__main__':
    with open("input.in") as f:
        input = f.read()
    input = list(int(x) for x in input)
    print("part 1: ", part_1(input))
    print("part 2: ", part_2(input))
