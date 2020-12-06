INPUT = "06.in"


def get_input():
    with open(INPUT, 'r') as f:
        return f.read().strip().split("\n\n")


def part1(inp):
    return sum(len(set(group.replace("\n", ""))) for group in inp)


def part2(inp):
    ans = 0
    for group in inp:
        all_present = set(chr(c) for c in range(ord('a'), ord('z') + 1))
        for person in group.splitlines():
            all_present = all_present.intersection(set(person))
        ans += len(all_present)
    return ans


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
