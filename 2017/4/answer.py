from collections import Counter


def is_anagram(a, b):
    return Counter(a) == Counter(b)


def p1(passwords):
    count = 0
    for p in passwords:
        words = p.split(' ')
        word_count = Counter(words)
        if word_count.most_common(1)[0][1] <= 1:
            count += 1
    return count


def p2(passwords):
    p2 = 0
    for p in passwords:
        words = p.split(' ')
        anagram_found = False
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if is_anagram(words[i], words[j]):
                    anagram_found = True
        if not anagram_found:
            p2 += 1
    return p2


if __name__ == '__main__':
    with open('input.in') as f:
        input = f.read()
    passwords = input.split('\n')
    print('part 1: ', p1(passwords))
    print('part 2: ', p2(passwords))
