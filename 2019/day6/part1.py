inp_file = open("input.txt")
pairs = [line.split(")") for line in inp_file.read().split()]
inp_file.close()

cache = {}


def orbits(satellite):
    if satellite in cache:
        return cache[satellite]
    for pair in pairs:
        if pair[1] == satellite:
            cache[satellite] = [pair[0]] + orbits(pair[0])
            return cache[satellite]
    return []


total = sum([len(orbits(satellite)) for centre, satellite in pairs])

print(total)
