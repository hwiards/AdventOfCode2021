from collections import defaultdict, Counter

def part1(data):
    numbers = defaultdict(int)
    num_lines = len(data)

    for line in data:
        for pos, char, in enumerate(line):
            if char == '1':
                numbers[pos] += 1

    num_bits = len(numbers)
    gamma, epsilon = '', ''
    for i in range(num_bits):
        if numbers[i] / num_lines >= 0.5:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def part2(data):
    size = len(data[0].strip())
    data_oxy = data.copy()
    for i in range(size):
        if len(data_oxy) == 1: break
        ones = [entry for entry in data_oxy if entry[i] == '1']
        zeros = [entry for entry in data_oxy if entry[i] == '0']
        data_oxy = ones if len(ones) >= len(zeros) else zeros
    oxy = int(data_oxy[0], 2)

    data_co2 = data.copy()
    for i in range(size):
        if len(data_co2) == 1: break
        ones = [entry for entry in data_co2 if entry[i] == '1']
        zeros = [entry for entry in data_co2 if entry[i] == '0']
        data_co2 = ones if len(ones) < len(zeros) else zeros
    co2 = int(data_co2[0], 2)

    return oxy * co2


if __name__ == '__main__':
    example = open("example.txt").readlines()
    input = open("input.txt").readlines()

    assert part1(example) == 198
    print(part1(input))

    assert part2(example) == 230
    print(part2(input))
