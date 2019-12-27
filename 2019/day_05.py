
from intcode import IntCode
import os


if __name__ == '__main__':
    filename = os.path.splitext(os.path.dirname(__file__))[
        0] + 'inputs/05.in'
    with open('inputs/05.in') as f:
        data = list(map(int, f.read().split(',')))

    vm = IntCode(data[:])
    print("part 2: ", vm.run([5]))
