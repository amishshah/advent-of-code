inp_file = open("input.txt")
pairs = [line.split(")") for line in inp_file.read().split()]
inp_file.close()


def connected(body):
    bodies = []
    for pair in pairs:
        if pair[0] == body:
            bodies.append(pair[1])
        elif pair[1] == body:
            bodies.append(pair[0])
    return bodies


def traverse(start="YOU", depth=1, visited=[]):
    visited = visited + [start]
    bodies = connected(start)
    distances = []
    for body in bodies:
        if body == "SAN":
            return depth
        if body not in visited:
            result = traverse(body, depth + 1, visited)
            if result:
                distances.append(result)
    return min(distances) if len(distances) > 0 else None


print(traverse() - 2)
