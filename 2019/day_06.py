import os


def part_1(input):
    total = 0
    s = {sat: orb for orb, sat in input}
    for sat in s.keys():
        while sat != "COM":
            sat = s[sat]
            total += 1
    return total


def part_2(input):
    s = {sat: orb for orb, sat in input}

    you_path = ["YOU"]
    santa_path = ["SAN"]

    # Generate paths from you and santa, to the central orbit
    while you_path[-1] != "COM":
        you_path.append(s[you_path[-1]])

    while santa_path[-1] != "COM":
        santa_path.append(s[santa_path[-1]])

    # Find the last common satelite, and reduce lists to be from this one
    while santa_path[-1] == you_path[-1]:
        santa_path = santa_path[:-1]
        you_path = you_path[:-1]

    return (len(santa_path) + len(you_path) - 2)


if __name__ == '__main__':
    filename = os.path.splitext(os.path.dirname(__file__))[
        0] + 'inputs/06.in'
    inp = [l.split(")") for l in open(filename).read().split('\n')]
    print("part 1: ", part_1(inp))
    print("part 2: ", part_2(inp))
