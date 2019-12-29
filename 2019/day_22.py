import re


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


def p1(instructions, card_length):
    cards = [i for i in range(0, card_length)]
    for instruction in instructions:
        code, value = process_instruction(instruction)
        if code == "cut":
            cards = cut(cards, value)
        elif code == "increment":
            cards = deal_inc(cards, value)
        elif code == "new_stack":
            cards = deal_new_stack(cards)
    return cards


if __name__ == "__main__":
    with open("inputs/22.in", "r") as f:
        instructions = f.read().split('\n')

    p1_deck = p1(instructions, 10007)

    print("part 1:", p1_deck.index(2019))

    print("part 2:")
