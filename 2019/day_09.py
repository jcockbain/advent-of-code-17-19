from intcode import IntCode
import os

if __name__ == '__main__':
    filename = os.path.splitext(os.path.dirname(__file__))[
        0] + 'inputs/09.in'
    file = open(filename, "r")
    data = list(map(lambda x: int(x), file.read().split(',')))
    vm = IntCode(data)
    print('Part 1: ', vm.run([1]))
    vm = IntCode(data)
    print('Part 2:', vm.run([2]))
