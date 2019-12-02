import re

input = open('input.txt').readlines()

int_list = list(map(int, re.findall(r'\d+', input[0])))


def part_1(x):
    x[1], x[2] = 2, 12
    return run_comp(x)


def part_2(x):
    for i in range(0, 99):
        for j in range(0, 99):
            x_copy = x.copy()
            x_copy[1], x_copy[2] = i, j
            if run_comp(x_copy)[0] == 19690720:
                return (100*i) + j
    return


def run_comp(x):
    for i in range(0, len(x), 4):
        if x[i] == 99:
            return x
        elif x[i] == 1:
            x[x[i+3]] = x[x[i + 1]] + x[x[i + 2]]
        elif x[i] == 2:
            x[x[i + 3]] = x[x[i + 1]] * x[x[i + 2]]
    return x


print(part_1(int_list.copy())[0])
print(part_2(int_list.copy()))
