from collections import defaultdict
from string import ascii_uppercase

import networkx as nx
import os


def get_nbs(point):
    return [(point[0] + dx, point[1] + dy) for dx, dy in zip([0, 1, 0, -1], [-1, 0, 1, 0])]


def create_grid(inp):
    grid = defaultdict(lambda: '#')
    W, H = len(inp[0]), len(inp)

    for y in range(H):
        for x in range(W):
            grid[(x, y)] = inp[y][x] if inp[y][x] != ' ' else '#'
    return grid


def p1(inp):
    W, H = len(inp[0]), len(inp)
    grid = create_grid(inp)

    # matches the portal names to their coordinates like portals['XY'] = [(x1,y1), (x2, y2)]
    portals = defaultdict(list)
    G = nx.Graph()
    start = end = None
    for y in range(1, H - 1):
        for x in range(1, W - 1):
            symbol = grid[(x, y)]
            if symbol in ascii_uppercase:
                nbs = [(a, b)
                       for a, b in get_nbs((x, y)) if grid[(a, b)] != '#']
                if len(nbs) == 2:
                    # letter and pathway found
                    if grid[nbs[0]] in ascii_uppercase:
                        letter, pad = nbs
                    else:
                        pad, letter = nbs
                    # sort portal name
                    key = ''.join(sorted(symbol + grid[letter]))
                    portals[key].append(pad)
                    if key == 'AA':
                        start = pad
                    elif key == 'ZZ':
                        end = pad
            elif symbol == '.':
                G.add_node((x, y))
                nbs = [(a, b)
                       for a, b in get_nbs((x, y)) if grid[(a, b)] == '.']
                for nb in nbs:
                    G.add_edge((x, y), nb)  # connect pathways

    for pads in portals.values():
        if len(pads) == 2:
            G.add_edge(pads[0], pads[1])  # connect portals

    return nx.shortest_path_length(G, start, end)


def p2(inp):
    W, H = len(inp[0]), len(inp)
    grid = create_grid(inp)

    # matches the portal names to their coordinates like portals['XY'] = [(x1,y1), (x2, y2)]
    portals = defaultdict(list)
    G = nx.Graph()
    levels = 30  # maximum allowed recursion depth
    start = end = None
    for y in range(1, H - 1):
        for x in range(1, W - 1):
            symbol = grid[(x, y)]
            if symbol in ascii_uppercase:
                nbs = [(a, b)
                       for a, b in get_nbs((x, y)) if grid[(a, b)] != '#']
                if len(nbs) == 2:
                    # letter and pathway found
                    if grid[nbs[0]] in ascii_uppercase:
                        letter, pad = nbs
                    else:
                        pad, letter = nbs
                    # sort portal name
                    key = ''.join(sorted(symbol + grid[letter]))
                    portals[key].append(pad)
                    if key == 'AA':
                        start = pad
                    elif key == 'ZZ':
                        end = pad
            elif symbol == '.':
                for i in range(levels):
                    G.add_node((x, y, i))  # create the node on each level
                nbs = [(a, b)
                       for a, b in get_nbs((x, y)) if grid[(a, b)] == '.']
                for nb in nbs:
                    for i in range(levels):
                        # connect the pathways on each level
                        G.add_edge((x, y, i), (*nb, i))

    for pads in portals.values():
        if len(pads) == 2:
            if pads[0][0] in [2, W - 3] or pads[0][1] in [2, H - 3]:
                outer, inner = pads
            else:
                inner, outer = pads
            for i in range(levels - 1):
                # inner portals lead to the outer portals on the next level and outer to inner on the previous level
                G.add_edge((*inner, i), (*outer, i + 1))
                G.add_edge((*outer, i + 1), (*inner, i))

    # specify that we want to start and end on level 0
    return nx.shortest_path_length(G, (*start, 0), (*end, 0))


if __name__ == "__main__":
    filename = os.path.splitext(os.path.dirname(__file__))[
        0] + 'inputs/20.in'

    with open(filename) as f:
        in1 = f.read().split('\n')

    print("part 1:", p1(in1[:]))
    print("part 2:", p2(in1[:]))
