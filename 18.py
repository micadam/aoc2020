from calc import calculate, setup

INPUT = "18.in"


def get_input():
    with open(INPUT, 'r') as f:
        return f.read().splitlines()


def part1(inp):
    setup("EVEN")
    return sum(calculate(line) for line in inp)


def part2(inp):
    setup("ADDITION_FIRST")
    return sum(calculate(line) for line in inp)


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
