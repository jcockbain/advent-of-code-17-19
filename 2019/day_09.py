from intcode import IntCode

if __name__ == '__main__':
    file = open('inputs/09.in', "r")
    data = list(map(lambda x: int(x), file.read().split(',')))
    vm = IntCode(data)
    print('Part 1: ', vm.run([1]))
    vm = IntCode(data)
    print('Part 2:', vm.run([2]))
