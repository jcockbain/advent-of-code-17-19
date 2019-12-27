import math


def find_layers(inp, w, h):
    size = w * h
    layers = [inp[i * size: (i+1) * size]
              for i in range(math.floor(len(inp) / size))]
    return layers


def part_1(inp, w, h):
    layers = find_layers(inp, w, h)
    counts = [layer.count(0) for layer in layers]
    min_index = counts.index(min(counts))
    return layers[min_index].count(1) * layers[min_index].count(2)


def part_2(inp, w, h):
    layers = find_layers(inp, w, h)
    size = w * h
    result = ["2"] * size
    for layer in layers:
        for i in range(size):
            if result[i] == "2":
                result[i] = str(layer[i])
    return result


def print_img(inp, w, h):
    current_width = 0
    for r in range(h):
        layer = "".join(inp[current_width: current_width + w])
        current_width += w
        print(layer.replace("0", ".").replace("1", "#"))


if __name__ == '__main__':
    inp = [int(l) for l in open('inputs/08.in').read()]
    print("part 1: ", part_1(inp, 25, 6))
    p2 = part_2(inp, 25, 6)
    print("part_2: ")
    print_img(p2, 25, 6)
