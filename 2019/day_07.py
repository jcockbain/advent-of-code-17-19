from intcode import IntCode
from itertools import permutations


def part_1(data):
    outputs = []
    for config in permutations(range(5)):
        d = data.copy()
        output = 0
        for i in range(len(config)):
            c = IntCode(d, lambda: i)
            output = c.run([config[i], output])
            outputs.append(output)
    return max(outputs)


if __name__ == '__main__':
    file = open('inputs/07.in', "r")
    data = list(map(lambda x: int(x), file.read().split(',')))
    print('part 1:', part_1(data))
    # print('part 2:', part_2(data))
    # file.close()
