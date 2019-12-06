def part_1(a):
    count = 0
    s = {sat: orb for orb, sat in a}
    tot = 0

    for u in s.keys():
        while u != "COM":
            u = s[u]
            tot += 1
    return tot


def part_2(a):
    s = {sat: orb for orb, sat in a}

    you_path = ["YOU"]
    while you_path[-1] != "COM":
        you_path.append(s[you_path[-1]])

    santa_path = ["SAN"]
    while santa_path[-1] != "COM":
        santa_path.append(s[santa_path[-1]])

    while santa_path[-1] == you_path[-1]:
        santa_path = santa_path[:-1]
        you_path = you_path[:-1]
    return (len(santa_path) + len(you_path) - 2)


if __name__ == '__main__':
    inp = [l.split(")") for l in open('input.in').read().split('\n')]
    print(inp)
    print("part 1: ", part_1(inp))
    print("part 2: ", part_2(inp))
