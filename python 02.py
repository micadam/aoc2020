import re

INPUT = "02.in"



if __name__ == "__main__":
    with open(INPUT, 'r') as f:
        inp = map(lambda x: re.split("- :", x), f.readlines())
    print(inp)
