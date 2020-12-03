INPUT = "03.in"
TREE = "#"


def get_input():
    with open(INPUT, 'r') as f:
        return f.read().splitlines()


def part1(inp):
    ans = 0
    for i in range(1, len(inp)):
        ans += 1 if inp[i][i * 3 % len(inp[i])] == TREE else 0
    return ans


def part2(inp):
    ans = 1
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    for right, down in slopes:
        count = 0
        for i in range(down, len(inp), down):
            count += 1 if inp[i][int(i / down) * right % len(inp[i])] == TREE else 0
        ans *= count
    return ans


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
