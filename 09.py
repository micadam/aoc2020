from math import inf

INPUT = "09.in"
PREAMBLE_LEN = 25


def get_input():
    with open(INPUT, 'r') as f:
        return list(map(int, f.read().splitlines()))


def part1(inp):
    stored_nums = {}
    for num in inp[:PREAMBLE_LEN]:
        if num not in stored_nums:
            stored_nums[num] = 0
        stored_nums[num] += 1
    for old_index, new_number in enumerate(inp[PREAMBLE_LEN:]):
        found = False
        for stored_num in stored_nums:
            is_double = 2 * stored_num == new_number
            if is_double and stored_nums[stored_num] >= 2 \
               or not is_double and new_number - stored_num in stored_nums:
                found = True
                break
        if not found:
            return new_number
        if new_number not in stored_nums:
            stored_nums[new_number] = 0
        stored_nums[new_number] += 1
        old_number = inp[old_index]
        stored_nums[old_number] -= 1
        if stored_nums[old_number] == 0:
            stored_nums.pop(old_number)
    return -1


def part2(inp):
    weak_number = 1309761972  # part1(inp)
    sum_all = [0]
    for num in inp:
        sum_all.append(sum_all[-1] + num)
    for i in range(len(inp)):
        for j in range(i + 1, len(inp) + 1):
            this_sum = sum_all[j] - sum_all[i]
            if this_sum == weak_number:
                mi = inf
                ma = -1
                for num in inp[i + 1:j + 1]:
                    mi = min(mi, num)
                    ma = max(ma, num)
                return mi + ma
    return -1


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
