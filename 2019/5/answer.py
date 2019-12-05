def getIntcodeParam(paramModes, data, pointer, param):
    type = 0
    try:
        type = int(paramModes[-param])
    except IndexError:
        pass
    if (type == 0):
        return data[data[pointer + param]]
    return data[pointer + param]


def op_sum(pointer, data, paramModes):
    data[data[pointer + 3]] = getIntcodeParam(
        paramModes, data, pointer, 1) + getIntcodeParam(
            paramModes, data, pointer, 2)
    return pointer + 4


def op_multiply(pointer, data, paramModes):
    data[data[pointer + 3]] = getIntcodeParam(
        paramModes, data, pointer, 1) * getIntcodeParam(
            paramModes, data, pointer, 2)
    return pointer + 4


def op_input(pointer, data, paramModes):
    data[data[pointer + 1]] = int(input("Type int: "))
    return pointer + 2


def op_output(pointer, data, paramModes):
    print(getIntcodeParam(paramModes, data, pointer, 1))
    return pointer + 2


def op_jump_if_true(pointer, data, paramModes):
    if (getIntcodeParam(paramModes, data, pointer, 1) != 0):
        return getIntcodeParam(paramModes, data, pointer, 2)
    else:
        return pointer + 3


def op_jump_if_false(pointer, data, paramModes):
    if (getIntcodeParam(paramModes, data, pointer, 1) == 0):
        return getIntcodeParam(paramModes, data, pointer, 2)
    else:
        return pointer + 3


def op_equal(pointer, data, paramModes):
    if (getIntcodeParam(paramModes, data, pointer, 1) ==
            getIntcodeParam(paramModes, data, pointer, 2)):
        data[data[pointer + 3]] = 1
    else:
        data[data[pointer + 3]] = 0
    return pointer + 4


def op_less_than(pointer, data, paramModes):
    if (getIntcodeParam(paramModes, data, pointer, 1) < getIntcodeParam(paramModes, data, pointer, 2)):
        data[data[pointer + 3]] = 1
    else:
        data[data[pointer + 3]] = 0
    pointer += 4


Operations = {
    1: op_sum,
    2: op_multiply,
    3: op_input,
    4: op_output,
    5: op_jump_if_true,
    6: op_jump_if_false,
    7: op_less_than,
    8: op_equal,
}


def processCode(data):
    pointer = 0
    while data[pointer] != 99:
        opcode = int(str(data[pointer])[-2:])
        paramModes = str(data[pointer])[:-2]
        pointer = Operations[opcode](pointer, data, paramModes)
    return data


if __name__ == '__main__':
    file = open('input.in', "r")
    data = list(map(lambda x: int(x), file.read().split(',')))
    processCode(data)
    file.close()
