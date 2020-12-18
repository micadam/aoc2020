from itertools import product

INPUT = "17.in"
ACTIVE = '#'


def get_dirs_with_zero(num_dimensions):
    return list(product(*[(-1, 0, 1) for i in range(num_dimensions)]))


def elementwise_add_tuples(x, y):
    return tuple(a + b for a, b in zip(x, y))


def get_input():
    with open(INPUT, 'r') as f:
        return f.read().splitlines()


def simulate(inp, num_dimensions):
    dirs_with_zero = get_dirs_with_zero(num_dimensions)
    dirs = [di for di in dirs_with_zero if sum(abs(dii) for dii in di) != 0]
    active_fields = set()
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            if c == ACTIVE:
                active_fields.add(tuple([x, y, *(0 for i in range(num_dimensions - 2))]))

    for i in range(6):
        fields_to_consider = set([elementwise_add_tuples(field, di)
                                  for field in active_fields for di in dirs_with_zero])
        new_active_fields = set()
        for field in fields_to_consider:
            active_neighbour_count = 0
            for di in dirs:
                new_field = elementwise_add_tuples(field, di)
                if new_field in active_fields:
                    active_neighbour_count += 1
                if active_neighbour_count > 3:
                    break
            if field in active_fields and active_neighbour_count in [2, 3]:
                new_active_fields.add(field)
            if active_neighbour_count == 3:
                new_active_fields.add(field)
        active_fields = new_active_fields
    return len(active_fields)


def part1(inp):
    return simulate(inp, 3)


def part2(inp):
    return simulate(inp, 4)


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
