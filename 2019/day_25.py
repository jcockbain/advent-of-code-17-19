from intcode import IntCode
import os

# all non-fatal items, excluding mug which is heavier than the limit
inventory = [
    'astronaut ice cream',
    'mouse',
    'easter egg',
    'wreath',
    'hypercube',
    'prime number',
    'ornament'
]

# path to pick up all required items, to arrive at pressure sensor
instructions = [
    'north',
    'take astronaut ice cream',
    'south',
    'west',
    'take mouse',
    'north',
    'take ornament',
    'west',
    'north',
    'take easter egg',
    'north',
    'west',
    'north',
    'take wreath',
    'south',
    'east',
    'south',
    'east',
    'take hypercube',
    'north',
    'east',
    'take prime number',
    'west',
    'south',
    'west',
    'south',
    'west',
    'west',
]


def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]


def get_all_permutations(inv):
    return powerset(inv)


find_items = list(map(ord, list('\n'.join(instructions) + '\n')))
drop_1 = []
for item in inventory:
    drop_string = "drop " + item
    drop_1.append(drop_string)
drop_items = list(map(ord, list('\n'.join(drop_1) + '\n')))

perms = get_all_permutations(inventory)

take = []
for perm in perms:
    for item in perm:
        take_string = "take " + item
        take.append(take_string)
    take.append("north")
    for item in perm:
        drop_string = "drop " + item
        take.append(drop_string)
take_items = list(map(ord, list('\n'.join(take) + '\n')))


def get_input(ascii_image, vm):
    if len(find_items) > 0:
        return find_items
    if len(drop_items) > 0:
        return drop_items
    if len(take_items) > 0:
        return take_items
    vm.halted = True


if __name__ == "__main__":
    ascii_image = []
    filename = os.path.splitext(os.path.dirname(__file__))[
        0] + 'inputs/25.in'
    with open(filename, "r") as f:
        file = f.read().strip()
    data = list(map(int, file.split(',')))
    vm = IntCode(data, lambda: get_input(ascii_image, vm))
    while not vm.halted:
        ascii_int = vm.run()
        ascii_image.append(chr(ascii_int))
        if chr(ascii_int) == "\n":
            message = ''.join(ascii_image)
            print(message)
            if "complete" in message:
                vm.halted = True
            ascii_image = []

    print(''.join(ascii_image))
