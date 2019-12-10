deltas = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}


def find_manhattan_min(path1, path2):
    p1_points, p1_steps = find_points(path1)
    p2_points, p2_steps = find_points(path2)
    intersections = p1_points & p2_points
    return min(abs(x) + abs(y) for x, y in intersections)


def find_steps_min(path1, path2):
    p1_points, p1_steps = find_points(path1)
    p2_points, p2_steps = find_points(path2)
    intersections = p1_points & p2_points
    return min(p1_steps[point] + p2_steps[point] for point in intersections)


def find_points(directions):
    steps, curr_x, curr_y = 0, 0, 0
    points = set()
    step_counts = {}
    for dir in directions.split(','):
        d, num_moves = dir[:1], int(dir[1:], 10)
        dx, dy = deltas[d]
        for _ in range(num_moves):
            curr_x += dx
            curr_y += dy
            steps += 1
            points.add((curr_x, curr_y))
            step_counts.setdefault((curr_x, curr_y), steps)
    return points, step_counts


if __name__ == '__main__':
    with open("input.in") as f:
        input = f.read()
    path1, path2 = input.strip().split('\n')
    print(path1)
    print('Part 1: ', find_manhattan_min(path1, path2))
    print('Part 2: ', find_steps_min(path1, path2))
