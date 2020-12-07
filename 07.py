import queue


INPUT = "07.in"
MY_BAG = "shiny gold bags"


def get_input():
    with open(INPUT, 'r') as f:
        lines = f.read().strip().splitlines()

    inp = []
    for line in lines:
        if "no other bags" in line:
            continue
        outer, inner = line.split(" contain ")
        inner = inner \
            .replace("bags", "bag") \
            .replace("bag", "bags") \
            .replace(".", "") \
            .split(", ")
        inp.append((outer, inner))
    return inp


def part1(inp):
    graph = {}
    for outer, inner in inp:
        inner = [bag.split(" ", 1)[1] for bag in inner]
        for bag in inner:
            if bag not in graph:
                graph[bag] = set()
            graph[bag].add(outer)
    visited = set([MY_BAG])
    que = queue.Queue()
    que.put(MY_BAG)
    while not que.empty():
        current = que.get()
        visited.add(current)
        if current not in graph:
            continue
        for bag in graph[current]:
            if bag not in visited:
                que.put(bag)
    return len(visited) - 1


def get_cost_part2(bag, graph, include_self=1):
    ans = include_self
    if bag in graph:
        for inner in graph[bag]:
            num, name = int(inner[0]), inner[1]
            ans += num * get_cost_part2(name, graph)
    return ans


def part2(inp):
    graph = {}
    for outer, inner in inp:
        inner = [bag.split(" ", 1) for bag in inner]
        graph[outer] = inner
    return get_cost_part2(MY_BAG, graph, include_self=0)


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
