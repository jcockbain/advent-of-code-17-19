from operator import add, mul
from collections import defaultdict

operation = {
    1: add,
    2: mul,
}


def int_code(seq, inp):
    print(f'Input: {inp}')
    i = 0
    mem = defaultdict(int, enumerate(map(int, seq)))
    output = []
    rb = 0
    while True:
        inst = mem[i]
        if inst == 99:
            return output
        a, b, c = 0, 0, 0
        if inst > 100:
            inst, params = inst % 100, inst // 100
            c = params % 10
            params //= 10
            b = params % 10
            params //= 10
            a = params % 10
            params //= 10
        if inst in [1, 2, 5, 6, 7, 8]:
            if c == 0:
                p1 = mem[mem[i + 1]]
            elif c == 1:
                p1 = mem[i + 1]
            elif c == 2:
                p1 = mem[rb + mem[i + 1]]

            if b == 0:
                p2 = mem[mem[i + 2]]
            elif b == 1:
                p2 = mem[i + 2]
            elif b == 2:
                p2 = mem[rb + mem[i + 2]]

            if a == 2:
                index = rb + mem[i + 3]
            else:
                index = mem[i + 3]

            if inst in [1, 2]:
                mem[index] = operation[inst](p1, p2)
                i += 4
            elif inst == 5:
                i = p2 if p1 != 0 else i + 3
            elif inst == 6:
                i = p2 if p1 == 0 else i + 3
            elif inst == 7:
                mem[index] = 1 if p1 < p2 else 0
                i += 4
            elif inst == 8:
                mem[index] = 1 if p1 == p2 else 0
                i += 4
        elif inst == 3:
            code = mem[i]
            if code // 100 == 2:
                mem[rb + mem[i + 1]] = inp
            else:
                mem[mem[i + 1]] = inp
            i += 2

        elif inst == 4:
            if c == 0:
                index = mem[i + 1]
            elif c == 1:
                index = i + 1
            elif c == 2:
                index = rb + mem[i + 1]
            output.append(mem[index])
            i += 2
        elif inst == 9:
            if c == 0:
                index = mem[i + 1]
            elif c == 1:
                index = i + 1
            elif c == 2:
                index = rb + mem[i + 1]
            rb += mem[index]
            i += 2

        else:
            print(f'Unhandled error on code: {seq[i]}')
            return [-2]


if __name__ == '__main__':
    file = open('input.in', "r")
    data = list(map(lambda x: int(x), file.read().split(',')))
    print('Part 1:')
    print(int_code(data[:], 1))
    print('Part 2:')
    print(int_code(data[:], 2))
    file.close()
