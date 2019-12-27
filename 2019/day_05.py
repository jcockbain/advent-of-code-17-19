
from intcode import IntCode


if __name__ == '__main__':
    with open('inputs/05.in') as f:
        data = list(map(int, f.read().split(',')))

    vm = IntCode(data[:])
    print("part 2: ", vm.run([5]))
