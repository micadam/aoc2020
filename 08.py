INPUT = "08.in"

ACC = "acc"
JMP = "jmp"
NOP = "nop"

OPCODES = {
    ACC: 0,
    JMP: 1,
    NOP: 2
}

INSTRUCTIONS = {
    OPCODES[ACC]: lambda val: (val, 1),
    OPCODES[JMP]: lambda val: (0, val),
    OPCODES[NOP]: lambda val: (0, 1)
}


def get_input():
    with open(INPUT, 'r') as f:
        ans = f.read().splitlines()
        ans = [an.split(" ") for an in ans]
        return [(OPCODES[instr], int(code)) for instr, code in ans]


def switch_between_jmp_and_nop(opcode):
    return 3 - opcode


def simulate(inp):
    """Returns:
    acc: value of acc once program terminates or repeats an instruction
    terminated: a boolean indicating whether it terminated
    """
    acc = 0
    pos = 0
    visited = set()
    terminated = False
    while pos not in visited:
        visited.add(pos)
        if pos >= len(inp):
            terminated = True
            break
        opcode, val = inp[pos]
        dacc, dpos = INSTRUCTIONS[opcode](val)
        acc += dacc
        pos += dpos
    return acc, terminated


def part1(inp):
    return simulate(inp)[0]


def part2(inp):
    for i, line in enumerate(inp):
        opcode, val = line
        if opcode in [OPCODES[JMP], OPCODES[NOP]]:
            new_opcode = switch_between_jmp_and_nop(opcode)
            inp[i] = (new_opcode, val)
            acc, terminated = simulate(inp)
            if terminated:
                return acc
            inp[i] = (opcode, val)
    return -1


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
