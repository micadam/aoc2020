import re

INPUT = "04.in"


class RegexpValidator:
    def __init__(self, pattern):
        self.pattern = re.compile(pattern)

    def is_valid(self, field):
        return self.pattern.fullmatch(field)


class RangeValidator:
    def __init__(self, min_limit, max_limit):
        self.min_limit = min_limit
        self.max_limit = max_limit

    def is_valid(self, field):
        return field.isnumeric() \
            and self.min_limit <= int(field) <= self.max_limit


class HeightValidator:
    unit_validators = {
        "cm": RangeValidator(150, 193),
        "in": RangeValidator(59, 76)
    }

    def is_valid(self, field):
        if len(field) < 2 or field[-2:] not in self.unit_validators:
            return False
        value, unit = field[:-2], field[-2:]
        return self.unit_validators[unit].is_valid(value)


def get_input():
    with open(INPUT, 'r') as f:
        passports_raw = re.split("\n\n", f.read())
        passports_split = map(lambda x: re.split("[ \n]+", x), passports_raw)
        return list(passports_split)


def part1(inp):
    required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    optional_field = "cid"
    ans = 0
    for passport in inp:
        present_fields = set()
        for value in passport:
            present_fields.add(value.split(':')[0])
        present_fields.discard(optional_field)
        ans += 1 if required_fields == present_fields else 0
    return ans


def part2(inp):
    required_fields = {
        "byr": RangeValidator(1920, 2002),
        "iyr": RangeValidator(2010, 2020),
        "eyr": RangeValidator(2020, 2030),
        "hgt": HeightValidator(),
        "hcl": RegexpValidator(r"#[0-9a-f]{6}"),
        "ecl": RegexpValidator(r"(amb|blu|brn|gry|grn|hzl|oth)"),
        "pid": RegexpValidator(r"[0-9]{9}")
    }
    optional_field = "cid"
    ans = 0
    for passport in inp:
        present_fields = set()
        for entry in passport:
            split = entry.split(":")
            if len(split) != 2:
                break
            key, value = split
            if key == optional_field:
                continue
            if key not in required_fields \
               or not required_fields[key].is_valid(value):
                break
            present_fields.add(key)
        ans += 1 if required_fields.keys() == present_fields else 0
    return ans


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
