
from intcode import IntCode
import os


def p2(data):
    vm = IntCode(data)
    return vm.run([5])


if __name__ == '__main__':
    filename = os.path.splitext(os.path.dirname(__file__))[
        0] + 'inputs/05.in'
    with open('inputs/05.in') as f:
        data = list(map(int, f.read().split(',')))

    print("part 2: ", p2(data[:]))
