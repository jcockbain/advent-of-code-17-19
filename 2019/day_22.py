import re
import os


def deal_new_stack(cards):
    return cards[::-1]


def cut(cards, n):
    return cards[n:] + cards[:n]


def deal_inc(cards, inc):
    position, positions = 0, {}
    for card in cards:
        positions[position] = card
        position = (position + inc) % len(cards)
    new_cards = [positions[key] for key in sorted(positions.keys())]
    return new_cards


def process_instruction(instruction):
    digits = re.findall(r'-?\d+', instruction)
    if "cut" in instruction:
        return "cut", int(digits[0])
    if "increment" in instruction:
        return "increment", int(digits[0])
    if "new stack" in instruction:
        return "new_stack", None
    raise Exception("Invalid instruction")


def shuffle_pack(cards, instructions):
    for instruction in instructions:
        code, value = process_instruction(instruction)
        if code == "cut":
            cards = cut(cards, value)
        elif code == "increment":
            cards = deal_inc(cards, value)
        elif code == "new_stack":
            cards = deal_new_stack(cards)
    return cards


def p1(instructions, card_length):
    cards = [i for i in range(0, card_length)]
    cards = shuffle_pack(cards, instructions)
    return cards.index(2019)


def modular_inv(n, cards):
    return pow(n, cards-2, cards)


def p2(instructions):
    shuffles = 101741582076661
    cards = 119315717514047
    single_pass_increment = 1
    single_pass_offset = 0
    for instruction in instructions:
        code, value = process_instruction(instruction)
        if code == "cut":
            single_pass_offset += value * single_pass_increment
            single_pass_offset %= cards
        elif code == "increment":
            single_pass_increment *= modular_inv(value, cards)
            single_pass_increment %= cards
        elif code == "new_stack":
            single_pass_increment *= -1
            single_pass_increment %= cards
            single_pass_offset += single_pass_increment
            single_pass_offset %= cards
    inc = pow(single_pass_increment, shuffles, cards)
    off = single_pass_offset * (1 - inc) * \
        modular_inv((1 - single_pass_increment) % cards, cards)
    off %= cards
    return (off + (2020 * inc)) % cards


if __name__ == "__main__":
    filename = os.path.splitext(os.path.dirname(__file__))[
        0] + 'inputs/22.in'
    with open(filename, "r") as f:
        instructions = f.read().split('\n')

    print("part 1:", p1(instructions, 10007))
    print("part 2:", p2(instructions))
