from intcode import IntCode
import os


def get_input(screen, paddle_x, ball_x):
    for pos, v in screen.items():
        if v == 4:  # Ball
            ball_x = pos[0]
        elif v == 3:  # Paddle
            paddle_x = pos[0]
    if paddle_x < ball_x:
        return 1  # Move right
    elif paddle_x > ball_x:
        return -1  # Move left
    elif paddle_x == ball_x:
        return 0  # Don't move


def p1(memory):
    screen, ball_x, paddle_x = {}, 0, 0
    ball_x = 0
    paddle_x = 0
    vm = IntCode(memory, get_input(screen, paddle_x, ball_x))
    screen = {}
    while not vm.halted:
        x, y, t_id = [vm.run() for _ in range(3)]
        if any(i is None for i in [x, y, t_id]):
            continue
        screen[(x, y)] = t_id
    return sum(1 for k, v in screen.items() if v == 2)


def p2(memory):
    screen, ball_x, paddle_x = {}, 0, 0
    memory[0] = 2
    vm = IntCode(memory, lambda: get_input(screen, paddle_x, ball_x))
    score = 0
    while not vm.halted:
        x, y, t_id = [vm.run() for _ in range(3)]
        if any(i is None for i in [x, y, t_id]):
            continue
        if x == -1 and y == 0:
            score = t_id
        else:
            screen[(x, y)] = t_id
    return score


if __name__ == "__main__":
    filename = os.path.splitext(os.path.dirname(__file__))[
        0] + 'inputs/13.in'
    with open(filename) as f:
        data = list(map(int, f.read().split(',')))

    data1, data2 = data[:], data[:]
    print("part 1:", p1(data1))
    print("part 2:", p2(data2))
