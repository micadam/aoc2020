INPUT = "15.in"


def get_input():
    with open(INPUT, 'r') as f:
        return list(map(int, f.read().split(',')))


def get_nth_number(inp, n):
    last_index = {}
    for i, num in enumerate(inp[:-1]):
        last_index[num] = i + 1
    last_num_spoken = inp[-1]
    for i in range(len(inp) + 1, n + 1):
        if last_num_spoken not in last_index:
            next_num = 0
        else:
            next_num = i - 1 - last_index[last_num_spoken]
        last_index[last_num_spoken] = i - 1
        last_num_spoken = next_num
    return last_num_spoken


def part1(inp):
    return get_nth_number(inp, 2020)


def part2(inp):
    return get_nth_number(inp, 30000000)


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
