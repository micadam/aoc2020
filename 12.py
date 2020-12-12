INPUT = "12.in"

EAST = 'E'
SOUTH = 'S'
WEST = 'W'
NORTH = 'N'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'

DIRECTIONS = {
    EAST: 0,
    SOUTH: 1,
    WEST: 2,
    NORTH: 3
}
MOVES = {
    DIRECTIONS[EAST]: (1, 0),
    DIRECTIONS[SOUTH]: (0, -1),
    DIRECTIONS[WEST]: (-1, 0),
    DIRECTIONS[NORTH]: (0, 1),
}

sin90x = [0, 1, 0, -1]
cos90x = [1, 0, -1, 0]


def elementwise_add_tuples(x, y, val):
    return tuple(a + b * val for a, b in zip(x, y))


def get_input():
    with open(INPUT, 'r') as f:
        lines = f.read().splitlines()
        return [(line[:1], int(line[1:])) for line in lines]


def part1(inp):
    face = DIRECTIONS[EAST]
    pos = (0, 0)
    for code, val in inp:
        if code in DIRECTIONS:
            pos = elementwise_add_tuples(pos, MOVES[DIRECTIONS[code]], val)
        elif code in [LEFT, RIGHT]:
            mul = -1 if code == LEFT else 1
            face = (face + (val * mul) // 90) % 4
        elif code == FORWARD:
            pos = elementwise_add_tuples(pos, MOVES[face], val)
    return sum(abs(i) for i in pos)


def part2(inp):
    pos = (0, 0)
    waypoint_pos = (10, 1)
    for code, val in inp:
        if code in DIRECTIONS:
            waypoint_pos = elementwise_add_tuples(waypoint_pos, MOVES[DIRECTIONS[code]], val)
        elif code in [LEFT, RIGHT]:
            mul = 1 if code == LEFT else -1
            val = (mul * val // 90) % 4
            x, y = waypoint_pos
            waypoint_pos = (cos90x[val] * x - sin90x[val] * y, sin90x[val] * x + cos90x[val] * y)
        elif code == FORWARD:
            pos = elementwise_add_tuples(pos, waypoint_pos, val)
    return sum(abs(i) for i in pos)


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
