puzzle_input = "146810-612564"
[lower, upper] = [int(x) for x in puzzle_input.split("-")]


def is_valid(n):
    s = [int(x) for x in str(n)]

    prior = s[0]
    seen_pairs = {x: 0 for x in s}
    for i in s[1:]:
        if i < prior:
            return False
        if i == prior:
            seen_pairs[i] += 1
        prior = i
    return any(seen_pairs[x] == 1 for x in seen_pairs)


print(len([x for x in range(lower, upper+1) if is_valid(x)]))
