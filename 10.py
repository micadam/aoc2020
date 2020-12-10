INPUT = "10.in"
MAX_JUMP = 3


def get_input():
    with open(INPUT, 'r') as f:
        return list(map(int, f.read().splitlines()))


def part1(inp):
    joltages = set(inp)
    current_joltage = 0
    found = True
    jumps = {i: 0 for i in range(1, MAX_JUMP + 1)}
    while found:
        found = False
        for jump in range(1, MAX_JUMP + 1):
            new_joltage = current_joltage + jump
            if new_joltage in joltages:
                current_joltage = new_joltage
                jumps[jump] += 1
                found = True
                break
    jumps[3] += 1
    return jumps[1] * jumps[3]


def part2(inp):
    tribonacci = [1]
    joltages = set(inp)
    device_joltage = max(joltages) + MAX_JUMP
    for joltage in range(1, device_joltage + 1):
        if joltage not in joltages and joltage != device_joltage:
            tribonacci.append(0)
            continue
        tribonacci.append(sum(tribonacci[max(0, joltage - MAX_JUMP):joltage]))
    print(tribonacci)
    return tribonacci[device_joltage]


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
