with open("input.txt") as data:
    total = sum([(int(x) // 3) - 2 for x in data.readlines()])
    print(total)
