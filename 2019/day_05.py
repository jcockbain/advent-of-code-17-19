
from intcode import IntCode


def p2(data):
    vm = IntCode(data)
    return vm.run([5])


if __name__ == '__main__':
    with open('inputs/05.in') as f:
        data = list(map(int, f.read().split(',')))

    print("part 2: ", p2(data[:]))
