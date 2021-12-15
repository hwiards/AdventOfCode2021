from collections import Counter

def part1(input, num_steps):

    # this does everything but scale.. :D

    template = list(input[0].strip())
    rules = dict(rule.strip().split(" -> ") for rule in input[2:])

    for _ in range(num_steps):
        for pos, vals in enumerate(zip(template[:-1], template[1:])):
            i,j = vals
            template.insert(2*pos+1, rules[i+j])
    cnt = Counter(template)
    return max(cnt.values()) - min(cnt.values())

def part2(input, num_steps):
    template = list(input[0].strip())
    pairs = Counter(["".join(a) for a in zip(template[:-1], template[1:])])
    letters = Counter(template)

    rules = dict(rule.strip().split(" -> ") for rule in input[2:])

    for _ in range(num_steps):
        for str, count in pairs.copy().items():
            insert = rules[str]
            letters[insert] += count
            a,b = str
            pairs[str] -= count
            pairs[a+insert] += count
            pairs[insert+b] += count

    return max(letters.values()) - min(letters.values())



if __name__ == '__main__':
    example = open('example.txt').readlines()
    input = open('input.txt').readlines()

    assert part1(example, 10) == 1588
    print(part1(input, 10))

    assert part2(example, 40) == 2188189693529
    print(part2(input, 40))
