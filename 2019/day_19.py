from intcode import IntCode
import os


def print_beam(points):
    beam = ""
    for y in range(50):
        for x in range(50):
            if (x, y) in points:
                beam += "#"
            else:
                beam += "."
            if x == 49:
                beam += "\n"
    print(beam)


def create_beam(inp):
    points = []
    for y in range(50):
        for x in range(50):
            vm = IntCode(inp)
            output = vm.run([x, y])
            if output == 1:
                points.append((x, y))
    return points


def check_points(points):
    for point in points:
        x, y = point
        req_points = [(x1, y) for x1 in range(x, x + 100)] + \
            [(x, y1) for y1 in range(y, y + 100)]
        if all(p in points for p in req_points):
            return point
    return None


def check_point(point, points):
    x, y = point
    req_points = [(x1, y) for x1 in range(x, x + 100)] + \
        [(x, y1) for y1 in range(y, y + 100)]
    if all(p in points for p in req_points):
        return True
    return False


def p1(inp):
    beam_points = create_beam(inp)
    return len(beam_points)


def check(inp, x, y):
    vm = IntCode(inp)
    return vm.run([x, y])


def p2(inp):
    x = y = 0
    while not check(inp, x+99, y):
        y += 1
        while not check(inp, x, y+99):
            x += 1
    return x*10000 + y


if __name__ == '__main__':
    filename = os.path.splitext(os.path.dirname(__file__))[
        0] + 'inputs/19.in'
    file = open(filename, 'r')
    data = file.read().strip()
    data = list(map(int, data.split(',')))
    print("part 1: ", p1(data[:]))
    print("part 2: ", p2(data[:]))
