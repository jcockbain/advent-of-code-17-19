from intcode import IntCode
import os


def run(code, input):
    vm = IntCode(code[:])
    return vm.run(input)


if __name__ == '__main__':
    filename = os.path.splitext(os.path.dirname(__file__))[
        0] + 'inputs/09.in'
    file = open(filename, "r")
    data = list(map(lambda x: int(x), file.read().split(',')))
    print('Part 1: ', run(data, [1]))
    print('Part 2:', run(data, [2]))
