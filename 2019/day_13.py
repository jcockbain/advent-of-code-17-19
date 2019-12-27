from intcode import IntCode


def get_input():
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


def display(grid):
    max_x = max(x for x, y in grid)
    max_y = max(y for x, y in grid)
    # print(max_x, max_y)
    screen = [[' ' for i in range(max_x+1)] for j in range(max_y+1)]
    for k, v in grid.items():
        x, y = k
        screen[y][x] = tile_ids[v]
    for line in screen:
        print(''.join(line))


if __name__ == "__main__":
    with open('inputs/13.in') as f:
        data = list(map(int, f.read().split(',')))

    # print(data)
    old_data = data[:]
    vm = IntCode(data, get_input)
    screen = {}
    tile_ids = {0: ' ', 1: '|', 2: '#', 3: '█', 4: '@'}
    while not vm.halted:
        x, y, t_id = [vm.run() for _ in range(3)]
        if any(i is None for i in [x, y, t_id]):
            continue
        screen[(x, y)] = t_id
    print("part 1: ")
    print(sum(1 for k, v in screen.items() if v == 2))

    # display(screen)

    old_data[0] = 2
    vm2 = IntCode(old_data, get_input)
    screen = {}
    i = 0
    inp = 0
    ball_x = 0
    paddle_x = 0
    score = 0
    while not vm2.halted:
        x, y, t_id = [vm2.run() for _ in range(3)]
        if any(i is None for i in [x, y, t_id]):
            continue
        if x == -1 and y == 0:
            score = t_id
        else:
            screen[(x, y)] = t_id

        # display(screen)
    print("part 2: ")
    print(score)
