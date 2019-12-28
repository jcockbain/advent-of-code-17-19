
from intcode import IntCode
import os

moves = [(None, None), (0, -1), (0, 1), (-1, 0), (1, 0)]


def p1(memory):
    vm = IntCode(memory, lambda: i)

    pos = (0, 0)
    queue = [(pos, [], 0)]
    visited = set([pos])
    isEmpty = set([pos])
    hasOxygen = set()
    while queue:
        cur, btpath, lenpath = queue.pop()

        for p in btpath:
            a = vm.run([p])
            assert(a == 1)

        for i in range(1, 5):
            npos = (cur[0]+moves[i][0], cur[1]+moves[i][1])
            nbtpath = btpath + [i]
            nlenpath = lenpath+1
            if npos not in visited:
                visited.add(npos)
                out = vm.run([i])
                if out == 1:
                    isEmpty.add(npos)
                    queue.append((npos, nbtpath, nlenpath))
                    if i == 1:
                        x = 2
                    elif i == 2:
                        x = 1
                    elif i == 3:
                        x = 4
                    elif i == 4:
                        x = 3
                    out = vm.run([x])
                    assert(out == 1)
                elif out == 2:
                    hasOxygen.add(npos)
                    return lenpath + 1

        for p in btpath[:: -1]:
            if p == 1:
                p = 2
            elif p == 2:
                p = 1
            elif p == 3:
                p = 4
            elif p == 4:
                p = 3
            out = vm.run([p])
            assert(out == 1)

    return None


if __name__ == "__main__":
    filename = os.path.splitext(os.path.dirname(__file__))[
        0] + 'inputs/15.in'
    with open(filename) as f:
        data = list(map(int, f.read().split(',')))

    print("part 1:", p1(data))
