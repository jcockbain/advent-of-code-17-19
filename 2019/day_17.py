from intcode import IntCode
import os


def get_intersections(view):
    w, h = len(view[0]), len(view)
    intersections = set()
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            try:
                if (view[y][x] == '#' and
                    view[y][x - 1] == '#' and
                    view[y][x + 1] == '#' and
                    view[y - 1][x] == '#' and
                        view[y + 1][x] == '#'):
                    intersections.add((x, y))
            except IndexError:
                print(x, y)
                raise
    return intersections


def print_view(view):
    res = ''.join(chr(v) for v in view if v is not None)
    print(res)


def p1(memory):
    vm = IntCode(memory)
    res = []
    while not vm.halted:
        res.append(vm.run())
    # print_view(res)
    view = ''.join(chr(v) for v in res if v is not None).strip().splitlines()
    intersections = get_intersections(view)
    return sum(x * y for x, y in intersections)


if __name__ == '__main__':
    filename = os.path.splitext(os.path.dirname(__file__))[
        0] + 'inputs/17.in'
    file = open(filename, 'r')
    data = file.read().strip()
    data = list(map(int, data.split(',')))
    d1, d2 = data[:], data[:]
    print("part 1: ", p1(d1))
