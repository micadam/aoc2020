from math import inf

INPUT = "13.in"


def xgcd(a, b):
    """
    Shoutout to wikipedia
    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_s, old_t


def crt_x(a1, a2, n1, n2, m1, m2):
    """
    shoutout to wikipedia
    https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    """
    return a1 * n2 * m2 + a2 * n1 * m1


def get_input():
    with open(INPUT, 'r') as f:
        return f.read().splitlines()


def part1(inp):
    mi_time_left = inf
    ans = None
    time, buses = (int(inp[0]), [int(x) for x in inp[1].split(",") if x.isnumeric()])
    for bus in buses:
        time_left = -time % bus
        if time_left < mi_time_left:
            mi_time_left = time_left
            ans = mi_time_left * bus
    return ans


def part2(inp):
    buses = [(i, int(x)) for i, x in enumerate(inp[1].split(",")) if x.isnumeric()]
    n_prev = buses[0][1]
    a_prev = n_prev - buses[0][0]
    for a, n in buses[1:]:
        a = n - a
        prev_bezout, bezout = xgcd(n_prev, n)
        x = crt_x(a_prev, a, prev_bezout, bezout, n_prev, n)
        n_prev = n_prev * n
        a_prev = x % n_prev
    return n_prev, a_prev, a_prev % n_prev


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
