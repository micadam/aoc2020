from math import inf

INPUT = "05.in"


def get_input():
    with open(INPUT, 'r') as f:
        return f.read().splitlines()


def get_binary(line):
    return line \
        .replace('F', '0') \
        .replace('B', '1') \
        .replace('L', '0') \
        .replace('R', '1')


def part1(inp):
    ma = -1
    for line in inp:
        ident = int(get_binary(line), 2)
        ma = max(ident, ma)
    return ma


def part2(inp):
    ma = -1
    mi = inf
    present = set()
    for line in inp:
        ident = int(get_binary(line), 2)
        ma = max(ident, ma)
        mi = min(ident, mi)
        present.add(ident)
    for i in range(mi + 1, ma):
        if i not in present:
            return i


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
