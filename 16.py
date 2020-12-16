from typing import List
from math import inf

INPUT = "16.in"


class Ticket:
    def __init__(self, data: List[int]):
        self.data = list(map(int, data))

    def __repr__(self):
        return f"[Ticket {' '.join(map(str, self.data))}]"


class Interval:
    def __init__(self, left: int, right: int, field: str):
        self.left = left
        self.right = right
        self.field = field

    def __repr__(self):
        return f"[Interval {self.left} {self.right} {self.field}]"


class IntervalTree:
    """Shoutout to wikipedia:
    https://en.wikipedia.org/wiki/Interval_tree
    Except this one returns the actual intervals, as opposed to just the number of overlaps.
    """

    def __init__(self, intervals: List[Interval]):
        self.cache = {}
        mi = inf
        ma = -inf
        for interval in intervals:
            mi = min(interval.left, mi)
            ma = max(interval.right, ma)
        x_center = (ma + mi) // 2
        s_left = []
        s_center = []
        s_right = []
        for interval in intervals:
            if interval.right < x_center:
                s_left.append(interval)
            elif interval.left > x_center:
                s_right.append(interval)
            else:
                s_center.append(interval)
        self.x_center = x_center
        self.left = IntervalTree(s_left) if len(s_left) > 0 else None
        self.right = IntervalTree(s_right) if len(s_right) > 0 else None
        self.sorted_lefts = sorted(s_center, key=lambda i: i.left)
        self.sorted_rights = sorted(s_center, key=lambda i: -i.right)

    def __repr__(self):
        return f"[IntervalTree x_center<{self.x_center}>" \
            f"left<{self.left}>" \
            f"right<{self.right}>] " \
            f"sorted_lefts<{self.sorted_lefts}> " \
            f"sorted_rights<{self.sorted_rights}>]"

    def get_intervals_overlapping(self, x: int) -> List[Interval]:
        if x in self.cache:
            return self.cache[x]
        if x == self.x_center:
            return self.sorted_lefts
        overlapping = self._get_overlapping_in_center(x)
        border_tree = self.left if x < self.x_center else self.right
        if border_tree is not None:
            overlapping.extend(border_tree.get_intervals_overlapping(x))
        self.cache[x] = overlapping
        return overlapping

    def _get_overlapping_in_center(self, x: int) -> List[Interval]:
        """Find the overlapping intervals inside s_center.
        when x <  x_center, this corresponds to (binary) searching for
            the largest left <= x
        when x > x_center, this corresponds to (binary) searching for
            the smallest right >= x
        """
        sorted_list = self.sorted_lefts if x < self.x_center \
            else self.sorted_rights
        val = (lambda i: i.left) if x < self.x_center \
            else (lambda i: -i.right)
        mul = 1 if x < self.x_center else -1

        # This should be a binary search, pls fix Adam
        # I mean it's fast anyway so what's the big deal am I right?
        # Could be faster...
        # But I got my 2 stars.
        for i in range(len(sorted_list)):
            if val(sorted_list[i]) > x * mul:
                return sorted_list[:i].copy()
        return sorted_list.copy()


def get_ticket_invalidness(ticket: Ticket, tree: IntervalTree) -> int:
    """Returns a ticket's invalidness
    """
    for value in ticket.data:
        if len(tree.get_intervals_overlapping(value)) == 0:
            return value
    return "valid"


def get_input():
    with open(INPUT, 'r') as f:
        parts = f.read().split("\n\n")
        intervals = []
        for field in parts[0].split('\n'):
            field_name, intervals_str = field.split(": ")
            intervals_list = intervals_str.split(" or ")
            for interval_in_list in intervals_list:
                left, right = interval_in_list.split("-")
                intervals.append(Interval(int(left), int(right), field_name))
        my_ticket = Ticket(parts[1].splitlines()[1].split(","))
        other_tickets_strs = map(lambda s: s.split(","),
                                 parts[2].splitlines()[1:])
        other_tickets = list(map(Ticket, other_tickets_strs))
        return intervals, my_ticket, other_tickets


def part1(inp):
    intervals, _, other_tickets = inp
    tree = IntervalTree(intervals)
    ans = 0
    for other_ticket in other_tickets:
        invalidness = get_ticket_invalidness(other_ticket, tree)
        ans += invalidness if invalidness != "valid" else 0
    return ans


def part2(inp):
    intervals, my_ticket, other_tickets = inp
    all_field_names = set(i.field for i in intervals)
    num_fields = len(all_field_names)
    tree = IntervalTree(intervals)
    possibilities = {i: all_field_names for i in range(num_fields)}
    for j, other_ticket in enumerate(other_tickets):
        if get_ticket_invalidness(other_ticket, tree) != "valid":
            continue
        for i, val in enumerate(other_ticket.data):
            possibilities_here = set(i.field for i in tree.get_intervals_overlapping(val))
            possibilities[i] = possibilities[i].intersection(possibilities_here)
    used_fields = set()
    fields_dictionary = {}
    sorted_indices = sorted(possibilities.items(), key=lambda item: len(item[1]))
    for i, possibilities_field in sorted_indices:
        actual_possibilities = possibilities_field.difference(used_fields)
        if len(actual_possibilities) > 1:
            # If this happens then I'm pretty sure there's multiple solutions?
            print("bad")
        field_name = actual_possibilities.pop()
        used_fields.add(field_name)
        fields_dictionary[field_name] = i
    relevant_fields = [my_ticket.data[v] for k, v in fields_dictionary.items() if k.startswith("departure")]
    ans = 1
    for val in relevant_fields:
        ans *= val
    return ans


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
