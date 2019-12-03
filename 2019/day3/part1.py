import re


# returns list of (direction, distance)
def parse_line(line):
    return [(x[0], int(x[1:])) for x in re.findall(r"([A-Z]\d+)", line)]


def points_visited(origin, translation):
    direction, distance = translation
    if direction == "U":
        return [add(current_position, (0, i)) for i in range(1, distance + 1)]
    elif direction == "R":
        return [add(current_position, (i, 0)) for i in range(1, distance + 1)]
    elif direction == "D":
        return [add(current_position, (0, -i)) for i in range(1, distance + 1)]
    elif direction == "L":
        return [add(current_position, (-i, 0)) for i in range(1, distance + 1)]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


with open("input.txt") as inp_file:
    [wire1, wire2] = [parse_line(line) for line in inp_file.readlines()]

    wire1_path = [(0, 0)]
    for translation in wire1:
        current_position = wire1_path[-1]
        wire1_path += points_visited(current_position, translation)

    wire2_path = [(0, 0)]
    for translation in wire2:
        current_position = wire2_path[-1]
        wire2_path += points_visited(current_position, translation)

    wire1_path = set(wire1_path)
    wire2_path = set(wire2_path)

    coords = wire1_path.intersection(wire2_path)
    coords.remove((0, 0))

    print(min([abs(x) + abs(y) for x, y in coords]))
