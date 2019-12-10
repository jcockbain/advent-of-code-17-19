import numpy as np
import operator


def slope(x1, y1, x2, y2):
    return abs((y2-y1)/(x2-x1))


def direction(x1, y1, x2, y2):
    if x2 >= x1 and y2 >= y1:
        return 1
    elif x2 >= x1 and y2 < y1:
        return 2
    elif x2 < x1 and y2 < y1:
        return 3
    elif x2 < x1 and y2 >= y1:
        return 4


def angle(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        angle = 0 if y2 > y1 else 180
    else:
        slope_, direction_ = slope(x1, y1, x2, y2), direction(x1, y1, x2, y2)
        atan = np.arctan(slope_)*180/(np.pi)
        if direction_ == 1:
            angle = 90 - atan
        elif direction_ == 2:
            angle = 180 - atan
        elif direction_ == 3:
            angle = 270 - atan
        elif direction_ == 4:
            angle = 360 - atan
    return round(angle, 2)


def p1(inp):
    seen_asteroids = []
    h, w = len(inp), len(inp[0])
    sky = {(x, y): inp[y][x] for y in range(h) for x in range(w)}
    ast_pos = []
    sight_count = {}
    for position in sky:
        if sky[position] is "#":
            ast_pos.append(position)
    for ast1 in ast_pos:
        angles = []
        for ast2 in ast_pos:
            if ast1 != ast2:
                angles.append(angle(ast1, ast2))
        unique_angles = set(angles)
        sight_count[ast1] = len(unique_angles)
    max_pos, max_val = max(sight_count.items(), key=operator.itemgetter(1))
    return max_pos, max_val


def p2(inp, laser_pos):
    seen_asteroids = []
    h, w = len(inp), len(inp[0])
    sky = {(x, y): inp[y][x] for y in range(h) for x in range(w)}
    ast_positions = []
    asteroid_map = {}
    for position in sky:
        if sky[position] == "#":
            ast_positions.append(position)
    for a_pos in ast_positions:
        if a_pos != laser_pos:
            a_angle = angle(laser_pos, a_pos)
            if a_angle in asteroid_map:
                asteroid_map[a_angle].append(a_pos)
            else:
                asteroid_map[a_angle] = [a_pos]
    c = 0
    for a in asteroid_map:
        c += len(asteroid_map[a])
    destroyed_list = []
    ang_list = sorted(asteroid_map)
    i = 0
    while len(destroyed_list) < len(ast_positions) - 1:
        ang = ang_list[i]
        locs = asteroid_map[ang]
        if len(locs) > 0:
            destroyed_list.append(locs.pop(0))
        i += 1
        if i == len(ang_list):
            print(len(destroyed_list))
            i = 0
    return destroyed_list[200][0]*100 + destroyed_list[200][1]


if __name__ == '__main__':
    with open('input.in', 'r') as f:
        file = f.read()
    inp = file.split('\n')
    max_pos, max_val = p1(inp)
    print('part 1: %s for pos %s' % (max_val, max_pos))
    print('part 2: ', p2(inp, max_pos))
