def part_1(board):
    [x.sort() for x in board]
    count = 0
    for r in board:
        count += r[-1] - r[0]
    return(count)


def part_2(board):
    [x.sort() for x in board]
    count = 0
    for r in board:
        r.reverse()
        for i in range(0, len(r)):
            for j in range(i+1, len(r)):
                result = r[i] % r[j]
                if result == 0:
                    count += r[i] / r[j]
    return(count)


if __name__ == '__main__':
    board = []
    input = open('input.in').readlines()
    input_list = [x.strip('\n') for x in input]
    i = [x.split('\t') for x in input_list]
    [board.append(list(map(int, r))) for r in i]
    print("part 1: ", part_1(board))
    print("part 2: ", part_2(board))
