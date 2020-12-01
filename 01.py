INPUT = '01.in'


def part1(inp):
    nums = set()
    for a in inp:
        b = 2020 - a
        if b in nums:
            return a * b
        nums.add(a)


def part2(inp):
    for i, a in enumerate(inp):
        target = 2020 - a
        nums = set()
        for b in inp[i + 1:]:
            c = target - b
            if c in nums:
                return a * b * c
            nums.add(b)


if __name__ == '__main__':
    with open(INPUT, 'r') as f:
        inp = [int(line) for line in f]
    print(f"part 1 {part1(inp)}")
    print(f"part 2 {part2(inp)}")
