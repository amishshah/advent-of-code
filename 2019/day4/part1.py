puzzle_input = "146810-612564"
[lower, upper] = [int(x) for x in puzzle_input.split("-")]


def is_valid(n):
    s = [int(x) for x in str(n)]

    prior = s[0]
    pair_flag = False
    for i in s[1:]:
        if i < prior:
            return False
        if i == prior:
            pair_flag = True
        prior = i
    return pair_flag


print(len([x for x in range(lower, upper+1) if is_valid(x)]))
