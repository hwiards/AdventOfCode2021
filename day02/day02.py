def part1(data):
    horizontal = 0
    depth = 0

    for line in data:
        key, num = line.strip().split()
        if key == 'forward':
            horizontal += int(num)
        elif key == 'up':
            depth -= int(num)
        elif key == 'down':
            depth += int(num)

    return abs(horizontal) * abs(depth)

def part2(data):
    horizontal = 0
    depth = 0
    aim = 0

    for line in data:
        key, num = line.strip().split()
        if key == 'forward':
            horizontal += int(num)
            depth += int(num) * aim
        elif key == 'up':
            aim -= int(num)
        elif key == 'down':
            aim += int(num)

    return abs(horizontal) * abs(depth)

if __name__ == '__main__':
    example = open('example.txt').readlines()
    input = open('input.txt').readlines()

    assert part1(example) == 150
    print(part1(input))

    assert part2(example) == 900
    print(part2(input))
