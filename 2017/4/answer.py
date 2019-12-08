def p1(words):
    count = 0
    for p in words:
        if len(p) == len(set(p)):
            count += 1
    return count


def p2(words):
    p2 = 0
    for p in words:
        if len(set(''.join(sorted(word)) for word in p)) == len(p):
            p2 += 1
    return p2


if __name__ == '__main__':
    passwords = [i.strip().split() for i in open('input.in', 'r').readlines()]
    print('part 1: ', p1(passwords))
    print('part 2: ', p2(passwords))
