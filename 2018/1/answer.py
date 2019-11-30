input = open('1.txt').readlines()
int_list = [int(x) for x in input]


def part_1(input):
    return sum(input)


def part_2(input):
    current_freq = 0
    i = 0
    input_length = len(input)
    seen_freq = set()
    while True:
        current_freq += input[i % input_length]
        if current_freq in seen_freq:
            return current_freq
        else:
            seen_freq.add(current_freq)
            i += 1


print(part_2(int_list))
