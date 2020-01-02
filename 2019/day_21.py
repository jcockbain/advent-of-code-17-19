from intcode import IntCode


def run_springscript(vm):
    ascii_image = []
    while True:
        ascii_int = vm.run()
        if ascii_int is None:
            break
        if ascii_int > 127:
            return ascii_int, ''.join(ascii_image)
        ascii_image.append(chr(ascii_int))
    return -1, ''.join(ascii_image)


def load_springscript(vm, script):
    ascii_chars = list(map(ord, list('\n'.join(script) + '\n')))
    while len(ascii_chars) > 0:
        vm.run(ascii_chars)


def get_damage(vm, script):
    load_springscript(vm, script)
    damage, ascii_image = run_springscript(vm)
    if ascii_image:
        print(ascii_image)
    return damage


def p1(memory):
    script = [
        'NOT A T',
        'NOT B J',
        'OR T J',
        'NOT C T',
        'OR T J',
        'AND D J',
        'WALK'
    ]
    vm = IntCode(memory)
    return get_damage(vm, script)


def p2(memory):
    script = [
        'NOT A T',
        'NOT B J',
        'OR T J',
        'NOT C T',
        'OR T J',
        'AND D J',
        'NOT E T',
        'NOT T T',
        'OR H T',
        'AND T J',
        'RUN']
    vm = IntCode(memory)
    return get_damage(vm, script)


def print_view(view):
    res = ''.join(chr(v) for v in view if v is not None)
    print(res)


if __name__ == "__main__":
    with open("inputs/21.in", "r") as f:
        file = f.read().strip()
    data = list(map(int, file.split(',')))
    print("part 1", p1(data[:]))
    print("part 2", p2(data[:]))
