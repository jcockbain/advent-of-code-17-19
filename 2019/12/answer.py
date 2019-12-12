import re
from copy import deepcopy
from itertools import count
import math


def parse_numbers(line, negatives=True):
    num_re = r'-?\d+' if negatives else r'\d+'
    return [int(n) for n in re.findall(num_re, line)]


def lcm(a, b):
    return a // math.gcd(a, b) * b


def step(positions, velocities):
    for j in range(4):
        for k in range(j + 1, 4):
            for d in range(3):
                if positions[j][d] < positions[k][d]:
                    velocities[j][d] += 1
                    velocities[k][d] -= 1
                elif positions[j][d] > positions[k][d]:
                    velocities[j][d] -= 1
                    velocities[k][d] += 1


def p1(moons, steps):
    positions = [parse_numbers(moons[l]) for l in range(len(moons))]
    velocities = [[0] * 3 for _ in range(len(moons))]
    for _ in range(steps):
        step(positions, velocities)
        for x in range(4):
            for d in range(3):
                positions[x][d] += velocities[x][d]

        energy = 0
        for pos, vel in zip(positions, velocities):
            pot = sum(abs(p) for p in pos)
            kin = sum(abs(p) for p in vel)
            energy += pot * kin
    return energy


def p2(moons):
    positions = [parse_numbers(moons[l]) for l in range(len(moons))]
    velocities = [[0] * 3 for _ in range(len(moons))]
    initial_positions = deepcopy(positions)
    initial_velocities = deepcopy(velocities)
    cycles = [None, None, None]

    for i in count(start=1):
        step(positions, velocities)

        for x in range(4):
            for d in range(3):
                positions[x][d] += velocities[x][d]

        for d in range(3):
            if cycles[d] is not None:
                continue
            for m in range(4):
                if positions[m][d] != initial_positions[m][d]:
                    break
                if velocities[m][d] != initial_velocities[m][d]:
                    break
            else:
                cycles[d] = i
        if all(cycles):
            return lcm(lcm(cycles[0], cycles[1]), cycles[2])


if __name__ == '__main__':
    with open("12.in", "r") as f:
        file = f.read()
    inp = file.split('\n')
    print("part 1: ", p1(deepcopy(inp), 1000))
    print("part 2: ", p2(deepcopy(inp)))
    f.close()
