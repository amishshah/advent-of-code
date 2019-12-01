def fuel_required(mass):
    required = (mass // 3) - 2
    if required < 0:
        return 0
    return required + fuel_required(required)


with open("input.txt") as data:
    total = sum([fuel_required(int(x)) for x in data.readlines()])
    print(total)
