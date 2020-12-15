INPUT = "14.in"


def get_input():
    with open(INPUT, 'r') as f:
        return f.read().splitlines()


def generate_addresses_recurse(address, start_index=0):
    for i, c in enumerate(address[start_index:]):
        if c == 'X':
            address[start_index + i] = '0'
            for address_from_call in generate_addresses_recurse(address, start_index + i + 1):
                yield address_from_call
            address[start_index + i] = '1'
            for address_from_call in generate_addresses_recurse(address, start_index + i + 1):
                yield address_from_call
            address[start_index + i] = 'X'
            return
    yield ''.join(address)


def generate_addresses(mask, original_address):
    address = []
    for i, c in enumerate(mask):
        if c == '0':
            address.append(original_address[i])
        else:
            address.append(c)
    for address_from_call in generate_addresses_recurse(address):
        yield address_from_call


def part1(inp):
    mem = {}
    for line in inp:
        op, val = line.split(" = ")
        if op == "mask":
            mask = val
        elif op.startswith("mem["):
            address = int(op[4:-1])
            binary_val = "{0:036b}".format(int(val))
            if address not in mem:
                mem[address] = 0
            word = []
            for i, c in enumerate(mask):
                if c == 'X':
                    word.append(binary_val[i])
                else:
                    word.append(c)
            mem[address] = int(''.join(word), 2)
    return sum(mem.values())


def part2(inp):
    mem = {}
    for line in inp:
        op, val = line.split(" = ")
        if op == "mask":
            mask = val
        elif op.startswith("mem["):
            val_int = int(val)
            original_address = "{0:036b}".format(int(op[4:-1]))
            for address in generate_addresses(mask, original_address):
                if address not in mem:
                    mem[address] = 0
                mem[address] = val_int
    return sum(mem.values())


if __name__ == "__main__":
    inp = get_input()
    print(f"part1: {part1(inp)}")
    print(f"part2: {part2(inp)}")
