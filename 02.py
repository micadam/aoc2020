import re

INPUT = "02.in"


def part1(inp):
    ans = 0
    for line in inp:
        min_limit, max_limit, char, text = line
        min_limit, max_limit = int(min_limit), int(max_limit)
        count = sum(1 for c in text if c == char)
        ans += 1 if min_limit <= count <= max_limit else 0
    return ans


def part2(inp):
    ans = 0
    for line in inp:
        idx1, idx2, char, text = line
        idx1, idx2 = int(idx1) - 1, int(idx2) - 1
        ans += 1 if (text[idx1] == char) ^ (text[idx2] == char) else 0
    return ans


if __name__ == "__main__":
    with open(INPUT, 'r') as f:
        inp = list(map(lambda x: re.split("[- :]+", x), f.readlines()))
    print(f"part 1: {part1(inp)}")
    print(f"part 2: {part2(inp)}")

