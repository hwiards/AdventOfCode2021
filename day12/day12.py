from collections import defaultdict


def calc(input):
    neighbours = defaultdict(list)
    for line in input:
        n1, n2 = line.strip().split('-')
        neighbours[n1].append(n2)
        neighbours[n2].append(n1)

    erg = search("start", set(), neighbours)
    erg2 = search("start", set(), neighbours, part2=True)
    return erg, erg2


def search(cave: str, seen: set, neighbours, part2=False):
    if cave == 'end':
        return 1
    if cave.islower():
        if cave in seen:
            if part2 and cave != 'start':
                part2 = False
            else:
                return 0
        seen = seen.union({cave})

    paths = 0
    for neighbour in neighbours[cave]:  # type: str
        paths += search(neighbour, seen, neighbours, part2)
    return paths


if __name__ == '__main__':
    example1 = open('example1.txt').readlines()
    example2 = open('example2.txt').readlines()
    example3 = open('example3.txt').readlines()
    input = open('input.txt').readlines()

    assert calc(example1) == (10, 36)
    assert calc(example2) == (19, 103)
    assert calc(example3) == (226, 3509)
    print(calc(input))
