from scipy.signal import convolve
import numpy as np
from typing import Set, Sequence, Tuple


def get_nbs(point):
    return [(point[0] + dx, point[1] + dy) for dx, dy in zip([0, 1, 0, -1], [-1, 0, 1, 0])]


def readmap(maplines: Sequence[str]) -> np.array:
    return np.array([
        c == "#" for line in maplines for c in line
    ]).reshape((5, -1))


def iter(grid):
    new_grid = {}
    for point in grid:
        alive_nbs = 0
        nbs = get_nbs(point)
        for n in nbs:
            if n in grid and is_alive(grid[n]):
                alive_nbs += 1
        if is_alive(grid[point]):
            new_grid[point] = "#" if alive_nbs == 1 else "."
        else:
            new_grid[point] = "#" if 1 <= alive_nbs <= 2 else "."
    return new_grid


def iter_2(grid):
    pass


def print_world(grid):
    x, y = 0, 0
    H, W = get_dimensions_of_grid(grid)
    result = ""
    for point in grid:
        result += grid[point]
        x += 1
        if x == W + 1 and y != H:
            y += 1
            x = 0
            result += "\n"
    return result


def get_grid(world):
    grid = {}
    W, H = len(world[0]), len(world)
    grid = {(x, y): world[y][x] for y in range(H) for x in range(W)}
    return grid


def is_alive(symbol):
    return symbol == "#"


def get_dimensions_of_grid(grid):
    keys = list(grid.keys())
    keys.sort()
    H, W = keys[-1]
    return H, W


def p1(data):
    history = []
    grid = get_grid(data)
    while True:
        grid = iter(grid)
        if grid in history:
            break
        history.append(grid)
    return get_biodiversity_rating(grid)


def p2(data, minutes):
    grid = get_grid(data)
    return data


def get_biodiversity_rating(grid):
    power = 0
    rating = 0
    H, W = get_dimensions_of_grid(grid)
    for y in range(H+1):
        for x in range(W+1):
            if grid[(x, y)] == "#":
                rating += 2 ** power
            power += 1
    return rating


def run_multidimensional(matrix: np.array, steps: int = 200) -> int:
    # 3d kernel; only those on the same level, not above or below
    kernel = np.array([
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 1, 0], [1, 0, 1], [0, 1, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ])
    matrix = np.pad(matrix[None], [((steps + 1) // 2,), (0,), (0,)])

    for _ in range(steps):
        # count neighbours on the same layer, then clear the hole
        counts = convolve(matrix, kernel, mode='same')
        counts[:, 2, 2] = 0
        # layer below, counts[:-1, ...] are updated from kernel[1:, ...].sum()s
        # cell above hole += top row next level
        counts[:-1, 1, 2] += matrix[1:,  0, :].sum(axis=1)
        # cell below hole += bottom row next level
        counts[:-1, 3, 2] += matrix[1:, -1, :].sum(axis=1)
        # cell left of hole += left column next level
        counts[:-1, 2, 1] += matrix[1:, :,  0].sum(axis=1)
        # cell right of hole += right column next level
        counts[:-1, 2, 3] += matrix[1:, :, -1].sum(axis=1)
        # layer above, counts[1-:, ...] slices are updated from kernel[:-1, ...] indices (true -> 1)
        # top row += cell above hole next level
        counts[1:,  0, :] += matrix[:-1, 1, 2, None]
        # bottom row += cell below hole next level
        counts[1:, -1, :] += matrix[:-1, 3, 2, None]
        # left column += cell left of hole next level
        counts[1:, :,  0] += matrix[:-1, 2, 1, None]
        # right column += cell right of hole next level
        counts[1:, :, -1] += matrix[:-1, 2, 3, None]

        # next step is the same as part 1:
        matrix = (
            # A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.
            (matrix & (counts == 1)) |
            # An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
            (~matrix & ((counts == 1) | (counts == 2)))
        )

    return matrix.sum()


# assert run_multidimensional(test_matrix, 10) == 99


if __name__ == "__main__":
    with open("inputs/24.in", "r") as f:
        file = f.read()
    data = file.split("\n")
    print("part 1:  ", p1(data))

    m = readmap(data[:])
    print("part 2: ", run_multidimensional(m))
