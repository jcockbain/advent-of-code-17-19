from operator import add, mul
from collections import defaultdict
from intcode import IntCode
import os


def run_robot(data, input):
    curr_pos = [0, 0]
    facing = 0
    dirs = {0: [0, -1], 1: [1, 0], 2: [0, 1], 3: [-1, 0]}
    panels = defaultdict(int)
    inp = input
    vm = IntCode(data)
    while True:
        inp = vm.run([inp])
        dir = vm.run()
        if vm.halted:
            break
        panels[tuple(curr_pos)] = inp
        facing += 1 if dir else -1
        facing %= 4
        curr_pos = [curr_pos[0] + dirs[facing]
                    [0], curr_pos[1] + dirs[facing][1]]
        inp = panels[tuple(curr_pos)]
    return panels


def display(panels):
    x, y = max(panels, key=lambda p: p[0])[
        0], max(panels, key=lambda p: p[1])[1]
    display = []
    for row in range(y+1):
        display.append([])
        for col in range(x+1):
            display[row].append(' ')

    for p, v in panels.items():
        x, y = p
        display[y][x] = v

    for line in display:
        print(''.join('█' if c == 1 else ' ' for c in line))


if __name__ == '__main__':
    filename = os.path.splitext(os.path.dirname(__file__))[
        0] + 'inputs/11.in'
    with open(filename) as f:
        data = list(map(int, f.read().split(',')))

    p1 = run_robot(data[:], 0)
    print("part 1: ", len(p1))

    p2 = run_robot(data[:], 1)
    print("part 2: \n")
    display(p2)
